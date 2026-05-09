# AGENTS

## Project Scope

This repository is the editable source for the lightweight SLG Steam prototype analysis site.

- Live site: `https://dingkx-slg.run.ingarena.net`
- Main source page: `website/steam原型数据分析.html`
- Maintenance guide: `docs/网站信息维护指南_WEBSITE_INFO_MAINTENANCE.md`
- SLG commercialization HV report: `docs/SLG行业养成商业化原型横纵分析报告_SLG_MONETIZATION_PROTOTYPE_HV_REPORT.md`
- Actual RUN publish directory: `/Users/ahs/Desktop/Git/tmp/dingkx_slg_publish`

## Working Rules

- Treat the HTML as a static report, not an app with a build step.
- When changing visible website content, update the maintenance guide in the same turn.
- When changing SLG commercialization archetype coverage, update the HV report, regenerate `website/reports/SLG行业养成商业化原型横纵分析报告.pdf`, and keep the website summary aligned.
- When changing PPT links or review scores, also check `ppt-master/projects/review-summary.md`.
- Commercialization tab is currently `v4.20`: the current modeling surface is 16 commercial/progression archetypes, not 8. The 8 supplemental samples must not be reintroduced as a separate large card layer. Keep them consolidated into the 16-archetype matrix, `.model-card-grid`, and `9 个题材 × 16 原型适配卡`.
- Direction D / Nightking should be treated as a Mafia-like high-CPI UA risk in the commercialization tab, not as a compliance-ban archetype.
- Direction names must be explicit, for example `方向 B：大陆酒店经营`, not only `方向 B`.
- Unknown or unverified data must stay `unknown` / `数据未公开`; do not invent numbers.

## Deployment

- Deployments go through the `run-platform-deploy` skill and its `run_deploy.py` helper.
- Use the helper with the subcommand before `--dir`, for example `python3 .../run_deploy.py doctor --dir /Users/ahs/Desktop/Git/tmp/dingkx_slg_publish`; placing `--dir` before the subcommand has been observed to fall back to the current working directory.
- Do not call the RUN REST API directly.
- `.runplatform.json` lives in the publish directory and contains secrets. Keep it untracked and protected by `**/.runplatform.json` in the workspace `.gitignore`.
- Before deploying, clean stale publish artifacts such as `.bak`, temporary screenshots, debug HTML, and old exports from `/Users/ahs/Desktop/Git/tmp/dingkx_slg_publish`.
- After deployment, verify the live URL returns HTTP 200, the PDF report URL returns HTTP 200, and the live HTML contains the current version string plus key changed text such as `v4.20`, `16 商业化养成原型`, and `高 CPI 买量风险` when applicable.

## Current External Links

- B 大陆酒店 Google Slides: `https://docs.google.com/presentation/d/1mGIqlni9nVlRl2w5sun3FW54X-pw63KLi-fSOiZ5zsA/edit?usp=sharing`
- C 地下拳馆 Google Slides: `https://docs.google.com/presentation/d/12sI9NErQgFLqp97hsEZYD-qHlbQDzimyVdi9oeoSM8w/edit?usp=sharing`
- I 动物联盟 Google Slides / PPTX cloud file: `https://docs.google.com/presentation/d/1NyFhmzUPGHLTeZWM3C_JsQiA8l7SqBEP/edit?usp=sharing&ouid=110387310515616113298&rtpof=true&sd=true` (`2026-04-30` covered with `I_动物联盟_动物庇护所+Zootopia情感叙事+My-Perfect-Hotel_20260421_000314.pptx`; file id unchanged)
- J 防疫区 / 检疫哨站 Google Slides: `https://docs.google.com/presentation/d/18ZNEqxgLdA9Wi7pjmSjGu1rcBYUpJL4SRee7TpIj3Xg/edit?usp=sharing`
