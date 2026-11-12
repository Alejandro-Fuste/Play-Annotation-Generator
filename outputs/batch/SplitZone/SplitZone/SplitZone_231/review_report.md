# Play-Annotation-Generator Annotation Review — SplitZone_231

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_231`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 12 | START | 13 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 12 | START | 13 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 12 | START | 13 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 12 | START | 13 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 12 | START | 13 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 12 | START | 13 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 12 | START | 13 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 12 | START | 13 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 12 | START | 13 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 12 | START | 13 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 12 | START | 13 | 249 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 247 | START | 247 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 250 | START | 262 | 272 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 250 | START | 250 | 343 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 250 | START | 250 | 282 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 250 | START | 250 | 362 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 250 | START | 250 | 362 |
| ✅ EXACT | `Action_SplitBlock` | TE | `2` | `2` | 257 | START | 257 | 362 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 261 | END | 247 | 261 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 263 | START | 263 | 279 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `19` | `19` | 280 | START | 280 | 323 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 362 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_SnapReceive` | 247 | 261 | 15 | inferred_complete_timeline |
| `Action_None` | 262 | 262 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 263 | 279 | 17 | inferred_complete_timeline |
| `Action_None` | 280 | 419 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 279 | 267 | inferred_complete_timeline |
| `Action_BallCarry` | 280 | 323 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 325 | 329 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 331 | 340 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 342 | 370 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 373 | 419 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 256 | 244 | inferred_complete_timeline |
| `Action_SplitBlock` | 257 | 362 | 106 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 249 | 237 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 343 | 94 | inferred_complete_timeline |
| `Action_ZoneBlock` | 350 | 362 | 13 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 249 | 237 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 282 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 314 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 317 | 362 | 46 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_BallSnap` | 247 | 261 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 262 | 272 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 302 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 312 | 362 | 51 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 249 | 237 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 362 | 113 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 249 | 237 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 362 | 113 | inferred_complete_timeline |
| `Action_None` | 363 | 419 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–304
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 291 | 45 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 304 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 417 | 171 | inferred_complete_timeline |
| `Action_None` | 419 | 419 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–377
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 377 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 246 | 234 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 13–381 | 207 | 15 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 13–385 | 239 | 12 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 13–419 | 405 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 24–128 | 11 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 25–140 | 113 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 45–70 | 26 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 216–249 | 28 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 251–311 | 37 | 7 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 268–419 | 146 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 268–270 | 3 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 327–350 | 11 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 363–399 | 21 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 369–409 | 6 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 379–408 | 11 | 3 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 391–392 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 398–419 | 20 | 3 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 400–419 | 20 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 409–414 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 113 frames exceeds threshold 90 frames [start=250, end=362].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 113 frames exceeds threshold 90 frames [start=250, end=362].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [247–261], lower_priority='Action_ZoneBlock' annotated_start=250, effective_Action_ZoneBlock_start=262.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 113 frames exceeds threshold 90 frames [start=250, end=362].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 113 frames exceeds threshold 90 frames [start=250, end=362].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 113 frames exceeds threshold 90 frames [start=250, end=362].
- ⚠️ Action 'Action_None' range [247-291] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-419] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-419] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-362] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [262-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-302] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-307] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-343] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-377] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-323] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [331-340] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [342-370] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [250-282] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [286-314] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-114] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-296] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-330] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-364] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-28] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-65] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-184] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-218] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-316] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-343] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-406] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-412] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-49] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-134] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-70] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-350] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-399] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-403] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-412] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-414] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>