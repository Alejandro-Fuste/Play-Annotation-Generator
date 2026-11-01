# Play-Annotation-Generator Annotation Review — InsideZoneRead_169

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_169`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 54 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `17` | `14` | 52 | START | 63 | 64 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 55 | START | 55 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 55 | START | 55 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 55 | START | 55 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 55 | START | 55 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 64 | END | 52 | 64 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 68 | START | 68 | 82 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 83 | START | 83 | 91 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `2` | `1` | 92 | START | 125 | 227 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 64 | 13 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 68 | 82 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 83 | 91 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 160 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 227 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 122 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 127 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 155 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 156 | 102 | inferred_complete_timeline |
| `Action_None` | 157 | 245 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 156 | 102 | inferred_complete_timeline |
| `Action_None` | 157 | 208 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 56 | 108 | 53 | inferred_complete_timeline |
| `Action_None` | 116 | 273 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 122 | 71 | inferred_complete_timeline |
| `Action_None` | 131 | 150 | 20 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 224 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 69 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 108 | 57 | inferred_complete_timeline |
| `Action_None` | 128 | 147 | 20 | inferred_complete_timeline |
| `Action_None` | 149 | 168 | 20 | inferred_complete_timeline |
| `Action_None` | 186 | 215 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 137 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 146 | 95 | inferred_complete_timeline |
| `Action_None` | 153 | 389 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 56–173 | 90 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 63–75 | 13 | 2 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 79–185 | 102 | 4 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 83–235 | 96 | 3 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 96–116 | 18 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 100–282 | 183 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 103–116 | 12 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 144–237 | 94 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 149–194 | 12 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 160–389 | 228 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 161–169 | 9 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 162–203 | 42 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 171–389 | 214 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 179–389 | 200 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 198–219 | 17 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 207–212 | 6 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 222–224 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 301–303 | 3 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 316–389 | 73 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 351–389 | 35 | 3 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 363–366 | 4 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 367–369 | 3 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 376–389 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `17` (Position_Unknown): Annotated start 52 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `2` (RB): Annotated start 92 != Inferred start 125

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 338: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 102 frames exceeds threshold 90 frames [start=55, end=156].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 101 frames exceeds threshold 90 frames [start=55, end=155].
- ⚠️ Action 'Action_None' range [157-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-227] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-127] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-282] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-183] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-203] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-373] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>