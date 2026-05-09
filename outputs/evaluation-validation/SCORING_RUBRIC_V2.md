# SLG Scoring Rubric V2

> Date: 2026-05-08
> Change: split "front-end hook quality" from "front-end audience can convert into backend pressure".

## Why V2 Exists

The original 7-dimension score over-rewarded entries with strong D0 attraction, especially RNG, collecting, and simulation-management hooks.

The missing question was not "can this attract users?" but:

> Will the users attracted by the front-end theme and play pattern accept the later survival pressure, war pressure, or numerical validation scene that the backend needs to monetize?

港口开箱 exposed this gap. It can attract RNG / collecting / simulation-management players very well, but those users are not automatically war, survival, alliance, or long-term competition users.

v4.29 adds an implementation rule: do not merge two market products only because they share a publisher or both sit in the light-SLG family. If the first-screen topic/play pattern differs, score them separately. Top War and Top Heroes are therefore separate objects: Top War is a merge/military entry, while Top Heroes is a vertical one-finger RPG/hero exploration entry.

## V2 Dimensions

| Dimension | Weight |
|---|---:|
| User trend fit | 12 |
| First-screen hook and D0 loop | 12 |
| Front-end audience and backend pressure fit | 15 |
| Lightweight granularity fit | 10 |
| SLG backend carrying capacity | 13 |
| Monetization anchors | 13 |
| UA and creative boundary | 13 |
| Verifiability and executability | 12 |

Total: 100.

## New Dimension Definition

**Front-end audience and backend pressure fit** asks whether the user group attracted by the first-screen play pattern can naturally convert into D7-D30 backend pressure.

High score:

- Survival entry attracts users who accept resource scarcity, external threats, alliance defense, and war pressure.
- Tower defense / tactical entry attracts users who accept later formation, heroes, troop upgrades, and battle validation.
- Criminal / territory business entry attracts users who accept family, routes, districts, and conflict pressure.

Low score:

- RNG / opening / collecting entry attracts users who mainly want drops, collections, and lucky outcomes, then the product suddenly asks them to join hard alliance war.
- Pure caring / shelter / cozy entry attracts users who want emotional care, then the product asks them to participate in destructive PvP.
- Hotel / service management entry attracts users who want optimization and operations, then the product shifts into mafia territory war without a soft bridge.

## Decision Bands

| Score | Decision |
|---:|---|
| 80-100 | Can enter project validation |
| 65-79 | Small-sample validation |
| 50-64 | Observe / gather more proof |
| <50 or hard-gate hit | Do not greenlight |
