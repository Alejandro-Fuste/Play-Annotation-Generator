# Play-Annotation-Generator Annotation Review — SplitZone_310

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_310`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 9
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_SplitBlock` | DT1 | defense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | RG | `12` | `12` | 33 | START | 33 | 44 |
| ✅ EXACT | `Action_SplitBlock` | DT1 | `3` | `3` | 43 | START | 43 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 45 | START | 45 | 50 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `14` | 45 | START | 45 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 45 | START | 45 | 54 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 45 | START | 45 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 45 | START | 48 | 66 |
| ✅ EXACT | `Action_SnapReceive` | LG | `8` | `8` | 47 | END | 33 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | LT | `6` | `6` | 55 | START | 55 | 74 |
| ✅ EXACT | `Action_Handoff` | LG | `8` | `8` | 67 | START | 67 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LT | `6` | `6` | 77 | START | 77 | 135 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT2 | `5` | `5` | 104 | START | 104 | 115 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 239 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 54 | 10 | inferred_complete_timeline |
| `Action_PressEdge` | 55 | 74 | 20 | inferred_complete_timeline |
| `Action_PressEdge` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 135 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 148 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 169 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 176 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 47 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 67 | 77 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_None` | 95 | 196 | 102 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 94 | 50 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_BallSnap` | 33 | 44 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 50 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 94 | 50 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 269 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 269 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SplitBlock` | 43 | 94 | 52 | inferred_complete_timeline |
| `Action_None` | 101 | 129 | 29 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_None` | 116 | 241 | 126 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 269 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 264 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 269 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 101 | 69 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–251 | 166 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–269 | 265 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–269 | 266 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–269 | 259 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–77 | 78 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–269 | 240 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–130 | 130 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–269 | 259 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 91–269 | 179 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 98–269 | 170 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 128–197 | 61 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 129–269 | 131 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 145–183 | 26 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 179–204 | 26 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 179–262 | 84 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 203–269 | 66 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 216–269 | 53 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 227–268 | 41 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 236–244 | 9 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 238–269 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 622: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 622: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [33-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [43-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-129] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-241] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [55-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-169] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-176] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-50] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-269] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-196] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-77] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-67] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-130] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-204] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-220] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-241] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-268] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>