# Play-Annotation-Generator Annotation Review — SplitZone_151

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_151`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 91
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
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 1 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 1 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 1 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 1 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 1 | START | 2 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 1 | START | 2 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 1 | START | 2 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 1 | START | 2 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 46 | START | 46 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 49 | START | 49 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 49 | START | 57 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 49 | START | 49 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `17` | 49 | START | 49 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 49 | START | 49 | 108 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `8` | `8` | 52 | START | 52 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 56 | END | 46 | 56 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 60 | START | 60 | 69 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `6` | 70 | START | 70 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_None` | 70 | 263 | 194 | inferred_complete_timeline |
| `Action_None` | 265 | 296 | 32 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 69 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 359 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 107 | 62 | inferred_complete_timeline |
| `Action_None` | 109 | 176 | 68 | inferred_complete_timeline |
| `Action_None` | 180 | 359 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 323 | 278 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 261 | 216 | inferred_complete_timeline |
| `Action_None` | 265 | 359 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 2–101
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 51 | 50 | inferred_complete_timeline |
| `Action_SplitBlock` | 52 | 101 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 146 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 318 | 159 | inferred_complete_timeline |
| `Action_None` | 320 | 359 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–71
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 71 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 137 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 160 | 359 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 117 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 148 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 159 | 1 | inferred_complete_timeline |
| `Action_None` | 160 | 263 | 104 | inferred_complete_timeline |
| `Action_None` | 267 | 359 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 2–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 48 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 108 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 160 | 359 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 114 | 69 | inferred_complete_timeline |
| `Action_None` | 127 | 288 | 162 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 308 | 3 | inferred_complete_timeline |
| `Action_None` | 321 | 359 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–90
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 90 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 125 | 80 | inferred_complete_timeline |
| `Action_None` | 133 | 359 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 359 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 128 | 83 | inferred_complete_timeline |
| `Action_None` | 130 | 149 | 20 | inferred_complete_timeline |
| `Action_None` | 153 | 359 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 359 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 119 | 74 | inferred_complete_timeline |
| `Action_None` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_None` | 141 | 352 | 212 | inferred_complete_timeline |
| `Action_None` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 359 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 359 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 251 | 206 | inferred_complete_timeline |
| `Action_None` | 253 | 359 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 45 | 44 | inferred_complete_timeline |
| `Action_None` | 46 | 359 | 314 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 113–359 | 237 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 118–187 | 13 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 121–359 | 238 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 156–359 | 204 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 302–311 | 8 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 303–314 | 12 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 324–359 | 36 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 338–340 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [46–56], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=57.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 111 frames exceeds threshold 90 frames [start=49, end=159].
- ⚠️ Action 'Action_None' range [46-107] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-176] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 160, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [160-318] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-323] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-114] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-308] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [52-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-125] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-359] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-148] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-296] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-352] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-108] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-263] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-346] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '34' has 1 frames without a visible bounding box.
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

</details>