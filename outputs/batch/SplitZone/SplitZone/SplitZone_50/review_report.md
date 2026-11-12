# Play-Annotation-Generator Annotation Review — SplitZone_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_50`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 17 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `15` | `14` | 65 | START | 65 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `10` | 70 | START | 70 | 93 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 70 | START | 70 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 70 | START | 83 | 97 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 70 | START | 70 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `7` | 70 | START | 70 | 112 |
| ✅ EXACT | `Action_SplitBlock` | TE | `8` | `8` | 73 | START | 73 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 82 | END | 65 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `4` | `4` | 96 | START | 96 | 131 |
| ⚠️ START CHANGED | `Action_BallCarry` | QB | `5` | `5` | 122 | START | 175 | 240 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 182 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–240
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 65 | 82 | 18 | inferred_complete_timeline |
| `Action_None` | 83 | 116 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 240 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 95 | 31 | inferred_complete_timeline |
| `Action_None` | 97 | 329 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SplitBlock` | 73 | 157 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 182 | 83 | inferred_complete_timeline |
| `Action_None` | 183 | 220 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 95 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 96 | 131 | 36 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 137 | 182 | 46 | inferred_complete_timeline |
| `Action_None` | 183 | 241 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 17–251
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 64 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 79 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 82 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 110 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 182 | 68 | inferred_complete_timeline |
| `Action_None` | 183 | 251 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 112 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 182 | 63 | inferred_complete_timeline |
| `Action_None` | 183 | 270 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 154 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 127 | 63 | inferred_complete_timeline |
| `Action_None` | 136 | 170 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 143 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 128 | 64 | inferred_complete_timeline |
| `Action_None` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 329 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 238 | 174 | inferred_complete_timeline |
| `Action_None` | 242 | 286 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 211 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 85 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 48–124 | 77 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 89–210 | 122 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 119–329 | 211 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 121–136 | 12 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 144–171 | 28 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 170–256 | 87 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 180–258 | 79 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 183–329 | 147 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 183–249 | 66 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 213–327 | 114 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 217–329 | 113 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 234–329 | 89 | 2 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `4` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `5` (QB): Annotated start 122 != Inferred start 175

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 113 frames exceeds threshold 90 frames [start=70, end=182].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 113 frames exceeds threshold 90 frames [start=70, end=182].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 113 frames exceeds threshold 90 frames [start=70, end=182].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [65–82], lower_priority='Action_ZoneBlock' annotated_start=70, effective_Action_ZoneBlock_start=83.
- ⚠️ Action 'Action_None' range [65-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-211] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [96-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-116] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-240] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [73-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [65-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-251] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-124] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-258] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-249] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-320] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '30' has 1 frames without a visible bounding box.
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

</details>