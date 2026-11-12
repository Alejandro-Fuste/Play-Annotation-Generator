# Play-Annotation-Generator Annotation Review — SplitZone_188

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_188`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 12 | START | 13 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 12 | START | 13 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 12 | START | 13 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 12 | START | 17 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 12 | START | 41 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 12 | START | 13 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 12 | START | 13 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 182 | START | 182 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 185 | START | 185 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `11` | 185 | START | 185 | 198 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 185 | START | 198 | 309 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 185 | START | 185 | 218 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 185 | START | 185 | 252 |
| ❌ MISSING SEGMENT | `Action_SplitBlock` | Position_Unknown | `16` | `16` | 189 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 195 | END | 182 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `15` | `15` | 203 | START | 203 | 208 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `8` | `8` | 213 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 309 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 41–419
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 59 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 114 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 181 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 182 | 195 | 14 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 203 | 208 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 419 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–195
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 84 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 129 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 17–218
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 38 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 72 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 125 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 178 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 218 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–252
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 184 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 252 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–419
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 110 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 181 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 182 | 194 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 309 | 112 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 419 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–224
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 184 | 172 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 198 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 224 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–320
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 105 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 184 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 221 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 226 | 309 | 84 | inferred_complete_timeline |
| `Action_None` | 310 | 320 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–230
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 181 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 230 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–262
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 181 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 262 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–254
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 38 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 98 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 181 | 80 | inferred_complete_timeline |
| `Action_None` | 182 | 243 | 62 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 181 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 255 | 74 | inferred_complete_timeline |
| `Action_None` | 263 | 332 | 70 | inferred_complete_timeline |
| `Action_None` | 343 | 348 | 6 | inferred_complete_timeline |
| `Action_None` | 350 | 419 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–351
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 86 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 181 | 91 | inferred_complete_timeline |
| `Action_None` | 182 | 274 | 93 | inferred_complete_timeline |
| `Action_None` | 276 | 295 | 20 | inferred_complete_timeline |
| `Action_None` | 301 | 330 | 30 | inferred_complete_timeline |
| `Action_None` | 334 | 343 | 10 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 181 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 419 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–314
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 181 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 314 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–132
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 132 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–283
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 181 | 169 | inferred_complete_timeline |
| `Action_None` | 182 | 275 | 94 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 71–88 | 18 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 190–419 | 222 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 195–357 | 127 | 7 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 220–229 | 10 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 235–419 | 144 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 237–244 | 8 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 244–327 | 79 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 267–277 | 11 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 275–419 | 131 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 277–324 | 37 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 294–419 | 121 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 294–317 | 17 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 300–348 | 42 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 329–419 | 85 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 343–354 | 12 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 355–368 | 13 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 367–369 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 373–381 | 9 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 392–419 | 28 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 394–397 | 4 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 411–419 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 185 != Inferred start 198
- ❌ Missing segment for action `Action_SplitBlock` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '8' has invalid range: start=213, end=195. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 125 frames exceeds threshold 90 frames [start=185, end=309].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 125 frames exceeds threshold 90 frames [start=185, end=309].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [182–195], lower_priority='Action_ZoneBlock' annotated_start=185, effective_Action_ZoneBlock_start=196.
- ⚠️ Segment 'Action_SplitBlock' for track '16' has invalid range: start=189, end=88. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [13-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-252] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-314] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-332] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-274] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-330] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-343] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [221-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [182-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-309] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-125] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-178] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [182-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [203-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-255] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-419] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-345] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-356] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-314] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-317] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-348] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-354] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-368] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-381] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>