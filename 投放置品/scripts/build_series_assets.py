#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SLG 投放札记系列 · 配图批处理调度器

一键跑完某一篇（或整个系列）的所有配图：
- 概念封面图（调 gen_images.py --batch）
- 信息图（调 gen_images.py --xhs）
- 游戏商店截图（调 fetch_game_assets.py --store-only）

用法：
    # 只跑 01 篇的所有图
    python3 scripts/build_series_assets.py --plan 01

    # 跑全部 5 篇
    python3 scripts/build_series_assets.py --all

    # 只跑生图（跳过游戏素材）
    python3 scripts/build_series_assets.py --plan 01 --images-only

    # 只抓游戏素材（跳过生图）
    python3 scripts/build_series_assets.py --plan 01 --games-only

    # 只看要执行什么命令，不真跑
    python3 scripts/build_series_assets.py --plan 01 --dry-run

    # 强制重新抓游戏（默认：本地已有就跳过）
    python3 scripts/build_series_assets.py --plan 01 --force-fetch

零依赖，只用 stdlib。
"""

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Dict, List, Optional

# ── 路径解析 ──────────────────────────────────────────────
SCRIPT_PATH = pathlib.Path(__file__).resolve()
SERIES_DIR = SCRIPT_PATH.parent.parent                         # drafts/SLG专题/投放札记/
DRAFTS_DIR = SERIES_DIR.parent.parent                           # drafts/ (跨过 SLG专题/)
PROJECT_DIR = DRAFTS_DIR.parent                                 # 丁开心的游戏观察/
SOURCES_DIR = PROJECT_DIR / "sources"

GEN_IMAGES = SOURCES_DIR / "gen_images.py"
FETCH_GAME_ASSETS = SOURCES_DIR / "fetch_game_assets.py"
GAME_ASSETS_CACHE = SOURCES_DIR / "game_assets"

PLANS_DIR = SERIES_DIR / "plans"
IMGS_DIR = SERIES_DIR / "imgs"
GAME_SCREENSHOTS_DIR = IMGS_DIR / "game_screenshots"


# ── 辅助 ─────────────────────────────────────────────────

def log(msg: str, indent: int = 0):
    print(("  " * indent) + msg, flush=True)


def run_cmd(cmd: List[str], dry_run: bool, cwd: Optional[pathlib.Path] = None) -> int:
    """跑一条命令。dry_run 模式下只打印不执行。"""
    pretty = " ".join(f'"{c}"' if " " in str(c) else str(c) for c in cmd)
    if dry_run:
        log(f"[DRY] {pretty}", indent=1)
        return 0

    log(f"$ {pretty}", indent=1)
    try:
        r = subprocess.run(cmd, cwd=cwd, check=False)
        if r.returncode != 0:
            log(f"    ⚠ 退出码 {r.returncode}", indent=1)
        return r.returncode
    except FileNotFoundError as e:
        log(f"    ✗ 命令未找到: {e}", indent=1)
        return 127


def load_plan(ep: str) -> Dict[str, Any]:
    plan_file = PLANS_DIR / f"{ep}.json"
    if not plan_file.exists():
        print(f"✗ plan 文件不存在: {plan_file}", file=sys.stderr)
        sys.exit(2)
    return json.loads(plan_file.read_text(encoding="utf-8"))


# ── 步骤 1 · 生成概念封面图 ────────────────────────────────

def build_concept_images(plan: Dict[str, Any], dry_run: bool):
    images = plan.get("concept_images") or []
    if not images:
        log("(无概念封面图)", indent=1)
        return

    IMGS_DIR.mkdir(parents=True, exist_ok=True)

    # 把 concept_images 写成临时 batch JSON（gen_images.py --batch 的 schema）
    batch_items = [
        {
            "name": img["name"],
            "prompt": img["prompt"],
            "size": img.get("size", "1920x1080"),
        }
        for img in images
    ]

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(batch_items, tmp, ensure_ascii=False, indent=2)
        tmp_path = tmp.name

    try:
        log(f"→ 概念图 {len(batch_items)} 张")
        for item in batch_items:
            log(f"  · {item['name']} ({item['size']})", indent=1)

        cmd = [
            sys.executable,
            str(GEN_IMAGES),
            "--batch", tmp_path,
            "--outdir", str(IMGS_DIR),
        ]
        run_cmd(cmd, dry_run=dry_run)
    finally:
        if not dry_run:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass


# ── 步骤 2 · 生成信息图 ────────────────────────────────────

def build_infographics(plan: Dict[str, Any], dry_run: bool):
    infos = plan.get("infographics") or []
    if not infos:
        log("(无信息图)", indent=1)
        return

    IMGS_DIR.mkdir(parents=True, exist_ok=True)

    log(f"→ 信息图 {len(infos)} 张")
    for i, info in enumerate(infos, 1):
        name = info["name"]
        out = IMGS_DIR / f"{name}.png"
        log(f"  [{i}/{len(infos)}] {name} ({info.get('layout', 'bento-grid')} / "
            f"{info.get('style', 'craft-handmade')} / {info.get('orientation', 'portrait')})", indent=1)

        cmd = [
            sys.executable,
            str(GEN_IMAGES),
            "--xhs", info["content"],
            "--layout", info.get("layout", "bento-grid"),
            "--style", info.get("style", "craft-handmade"),
            "--orientation", info.get("orientation", "portrait"),
            "--out", str(out),
        ]
        run_cmd(cmd, dry_run=dry_run)


# ── 步骤 3 · 抓游戏商店截图 + 同步到系列 imgs/ ─────────────

def fetch_and_sync_games(plan: Dict[str, Any], dry_run: bool, force_fetch: bool):
    games = plan.get("games") or []
    if not games:
        log("(无游戏素材)", indent=1)
        return

    GAME_SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    log(f"→ 游戏素材 {len(games)} 款")
    for i, game in enumerate(games, 1):
        display = game["display_name"]
        store_dir_name = game["store_dir_name"]
        local_cache = GAME_ASSETS_CACHE / store_dir_name
        target_dir = GAME_SCREENSHOTS_DIR / store_dir_name

        log(f"  [{i}/{len(games)}] {display} → {store_dir_name}", indent=1)
        if game.get("notes"):
            log(f"    ({game['notes']})", indent=1)

        # Step 3a: 如果本地缓存没有或强制重抓，跑 fetch_game_assets.py
        need_fetch = force_fetch or not local_cache.exists() or not any(local_cache.iterdir()) if local_cache.exists() else True
        if local_cache.exists() and not force_fetch:
            need_fetch = False

        if need_fetch:
            cmd = [sys.executable, str(FETCH_GAME_ASSETS), display, "--store-only"]
            for key, flag in [("appstore_id", "--appstore-id"),
                               ("gplay_id", "--gplay-id"),
                               ("steam_id", "--steam-id")]:
                val = game.get(key)
                if val:
                    cmd.extend([flag, str(val)])
            run_cmd(cmd, dry_run=dry_run, cwd=SOURCES_DIR)
        else:
            log(f"    · 本地缓存已有，跳过抓取（用 --force-fetch 强制重抓）", indent=1)

        # Step 3b: 把 local_cache 同步到 series imgs/game_screenshots/
        if dry_run:
            log(f"    [DRY] rsync {local_cache}/ → {target_dir}/", indent=1)
            continue

        if not local_cache.exists():
            log(f"    ⚠ 本地缓存仍不存在，跳过同步: {local_cache}", indent=1)
            continue

        if target_dir.exists():
            shutil.rmtree(target_dir)
        try:
            shutil.copytree(local_cache, target_dir, dirs_exist_ok=True)
            n_files = sum(1 for _ in target_dir.rglob("*") if _.is_file())
            log(f"    ✓ 同步 {n_files} 个文件 → {target_dir.relative_to(SERIES_DIR)}", indent=1)
        except Exception as e:
            log(f"    ✗ 同步失败: {e}", indent=1)


# ── 总调度 ───────────────────────────────────────────────

def run_episode(ep: str, dry_run: bool, images_only: bool, games_only: bool, force_fetch: bool):
    plan = load_plan(ep)
    log(f"━━━━ 第 {ep} 篇 · {plan['title']} ━━━━")
    log(f"副标题: {plan['subtitle']}", indent=1)

    if not games_only:
        build_concept_images(plan, dry_run)
        build_infographics(plan, dry_run)

    if not images_only:
        fetch_and_sync_games(plan, dry_run, force_fetch)

    log("")


def main():
    parser = argparse.ArgumentParser(description="SLG 投放札记系列配图批处理调度器")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--plan", help="跑指定篇（如 01/02/03/04/05）")
    g.add_argument("--all", action="store_true", help="跑全部 5 篇")

    parser.add_argument("--images-only", action="store_true", help="只生图，不抓游戏")
    parser.add_argument("--games-only", action="store_true", help="只抓游戏，不生图")
    parser.add_argument("--dry-run", action="store_true", help="只打印命令，不执行")
    parser.add_argument("--force-fetch", action="store_true", help="强制重抓游戏素材（默认跳过已有缓存）")

    args = parser.parse_args()

    # 健康检查
    for tool in (GEN_IMAGES, FETCH_GAME_ASSETS):
        if not tool.exists():
            print(f"✗ 缺少依赖脚本: {tool}", file=sys.stderr)
            sys.exit(3)

    if not PLANS_DIR.exists():
        print(f"✗ plans 目录不存在: {PLANS_DIR}", file=sys.stderr)
        sys.exit(3)

    if args.all:
        episodes = sorted(p.stem for p in PLANS_DIR.glob("*.json"))
        if not episodes:
            print("✗ 未找到任何 plan 文件", file=sys.stderr)
            sys.exit(3)
    else:
        episodes = [args.plan]

    log(f"系列目录: {SERIES_DIR}")
    log(f"将处理 {len(episodes)} 篇: {', '.join(episodes)}")
    log(f"dry-run: {args.dry_run}")
    log(f"images-only: {args.images_only}")
    log(f"games-only: {args.games_only}")
    log(f"force-fetch: {args.force_fetch}")
    log("")

    for ep in episodes:
        run_episode(ep,
                    dry_run=args.dry_run,
                    images_only=args.images_only,
                    games_only=args.games_only,
                    force_fetch=args.force_fetch)

    log("━━━━ 全部处理完成 ━━━━")


if __name__ == "__main__":
    main()
