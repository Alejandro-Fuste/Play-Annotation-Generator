# Play-Annotation-Generator Annotation Review — JetSweep_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_50`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_LeadBlock` | LB1 | defense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE2 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `21` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `16` | `15` | 17 | START | 17 | 78 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 48 | START | 48 | 63 |
| ✅ EXACT | `Action_LeadBlock` | LB1 | `17` | `16` | 50 | START | 50 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 50 | START | 50 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 50 | START | 50 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 50 | START | 64 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 50 | START | 50 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 50 | START | 50 | 72 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `18` | `17` | 63 | END | 48 | 63 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 69 | START | 69 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `16` | `15` | 79 | START | 79 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE2 | `2` | `1` | 83 | START | 83 | 103 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_Toss` | 69 | 78 | 10 | inferred_complete_timeline |
| `Action_None` | 79 | 266 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 389 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_JetMotion` | 17 | 78 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 144 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 166 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 170 | 377 | 208 | inferred_complete_timeline |
| `Action_BallCarry` | 379 | 382 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 297 | 250 | inferred_complete_timeline |
| `Action_None` | 302 | 374 | 73 | inferred_complete_timeline |
| `Action_None` | 377 | 380 | 4 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 110 | 63 | inferred_complete_timeline |
| `Action_None` | 116 | 178 | 63 | inferred_complete_timeline |
| `Action_None` | 180 | 253 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 83 | 103 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 389 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 75 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 86 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 68 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 109 | 39 | inferred_complete_timeline |
| `Action_None` | 110 | 296 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 99 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 72 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 99 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 108 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 217 | 96 | inferred_complete_timeline |
| `Action_None` | 228 | 285 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 83 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 337 | 290 | inferred_complete_timeline |
| `Action_None` | 339 | 389 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 64 | 389 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 140 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 358 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_LeadBlock` | 50 | 98 | 49 | inferred_complete_timeline |
| `Action_None` | 111 | 152 | 42 | inferred_complete_timeline |
| `Action_None` | 157 | 389 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 315 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 389 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 303 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 389 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 168 | 121 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 275 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 389 | 342 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 83–359 | 271 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 92–352 | 258 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 119–296 | 174 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 155–262 | 108 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 224–233 | 9 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 350–362 | 13 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 361–373 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=64.
- ⚠️ Action 'Action_None' range [48-358] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [83-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 110, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [110-112] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-337] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-178] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-266] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-72] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-99] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-217] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-285] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-303] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-389] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 110, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [110-296] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [170-377] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [379-382] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [50-98] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-315] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-297] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-374] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-206] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-321] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-352] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-296] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-362] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-373] for track '29' has 1 frames without a visible bounding box.
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

</details>