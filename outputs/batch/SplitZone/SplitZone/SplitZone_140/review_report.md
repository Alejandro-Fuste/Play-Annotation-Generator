# Play-Annotation-Generator Annotation Review — SplitZone_140

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_140`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 26 | START | 27 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 26 | START | 27 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 26 | START | 27 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 26 | START | 27 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 26 | START | 27 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 26 | START | 27 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 26 | START | 27 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 26 | START | 27 | 76 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 68 | START | 68 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 71 | START | 71 | 166 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 71 | START | 81 | 172 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 71 | START | 71 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 71 | START | 71 | 172 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 71 | START | 71 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `8` | `8` | 77 | START | 77 | 164 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 80 | END | 68 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `2` | `2` | 112 | START | 112 | 131 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `5` | 127 | START | 127 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 172 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 126 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 359 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–358
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 358 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 27–259
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 76 | 50 | inferred_complete_timeline |
| `Action_SplitBlock` | 77 | 164 | 88 | inferred_complete_timeline |
| `Action_SplitBlock` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 198 | 26 | inferred_complete_timeline |
| `Action_None` | 204 | 244 | 41 | inferred_complete_timeline |
| `Action_None` | 248 | 259 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 27–162
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 70 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 162 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 27–208
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 70 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 111 | 41 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 133 | 148 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 151 | 172 | 22 | inferred_complete_timeline |
| `Action_None` | 173 | 208 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 27–347
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 172 | 92 | inferred_complete_timeline |
| `Action_None` | 173 | 347 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–274
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 70 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 172 | 102 | inferred_complete_timeline |
| `Action_None` | 173 | 274 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 27–276
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 70 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 166 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 276 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 143 | 76 | inferred_complete_timeline |
| `Action_None` | 160 | 172 | 13 | inferred_complete_timeline |
| `Action_None` | 177 | 359 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 27–266
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 266 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 231 | 147 | inferred_complete_timeline |
| `Action_None` | 233 | 242 | 10 | inferred_complete_timeline |
| `Action_None` | 244 | 359 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 359 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 359 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 27–219
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 156 | 89 | inferred_complete_timeline |
| `Action_None` | 212 | 219 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 27–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 68 | 164 | 97 | inferred_complete_timeline |
| `Action_None` | 172 | 359 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 132–164 | 33 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 143–359 | 181 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 154–359 | 195 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 173–359 | 187 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 182–306 | 123 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 213–359 | 147 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 221–359 | 127 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 240–244 | 5 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 282–359 | 78 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 283–359 | 76 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 293–359 | 67 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 298–359 | 62 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 71 != Inferred start 81
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 102 frames exceeds threshold 90 frames [start=71, end=172].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 92 frames exceeds threshold 90 frames [start=71, end=162].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 102 frames exceeds threshold 90 frames [start=71, end=172].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 102 frames exceeds threshold 90 frames [start=71, end=172].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=81.
- ⚠️ Action 'Action_None' range [68-358] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [112-131] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [133-148] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [77-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-143] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-347] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-231] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-213] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-357] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>