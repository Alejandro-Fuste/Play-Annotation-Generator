# Play-Annotation-Generator Annotation Review — InsideZoneRead_169

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_169`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 9
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
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
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | DT1 | defense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | DT1 | defense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_Handoff` | DT1 | defense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 245 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `17` | `14` | 408 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `1` | `0` | 410 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `10` | `9` | 410 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `11` | `10` | 410 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `9` | `8` | 410 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | DT1 | `12` | `11` | 422 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | DT1 | `12` | `11` | 425 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | DT1 | `12` | `11` | 440 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `13` | `12` | 453 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 505 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |

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
| `Action_PreSnap` | 125 | 227 | 103 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 127 | 3 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |

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
| `Action_PreSnap` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 108 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 273 | 158 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 150 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 224 | 22 | inferred_complete_timeline |

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
| `Action_PreSnap` | 62 | 69 | 8 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 147 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 168 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 215 | 30 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 389 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 56–173 | 90 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 63–75 | 13 | 1 | Undefined position; Undefined team |
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

- ❌ Missing segment for action `Action_BallSnap` on target `14` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `10` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (RG)
- ❌ Missing segment for action `Action_SnapReceive` on target `12` (DT1)
- ❌ Missing segment for action `Action_ReadDefender` on target `12` (DT1)
- ❌ Missing segment for action `Action_Handoff` on target `12` (DT1)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (Position_Unknown)

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
| Track-related warning | 10 |
| Other | 12 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 338: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '0' has invalid range: start=410, end=208. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=410, end=245. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '9' has invalid range: start=410, end=127. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=410, end=155. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '11' has invalid range: start=408, end=69. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '11' has invalid range: start=425, end=69. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '11' has invalid range: start=440, end=69. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '12' has invalid range: start=453, end=1. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=408, end=75. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-227] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-127] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-282] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-116] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-183] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-169] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-203] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-219] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-373] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-381] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-366] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-369] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_BallSnap' has invalid start frame 408. Video range is [0, 389].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 410. Video range is [0, 389].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 410. Video range is [0, 389].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 410. Video range is [0, 389].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 410. Video range is [0, 389].
- ⚠️ Action event 'Action_SnapReceive' has invalid start frame 422. Video range is [0, 389].
- ⚠️ Action event 'Action_ReadDefender' has invalid start frame 425. Video range is [0, 389].
- ⚠️ Action event 'Action_Handoff' has invalid start frame 440. Video range is [0, 389].
- ⚠️ Action event 'Action_BallCarry' has invalid start frame 453. Video range is [0, 389].
- ⚠️ Action event 'Action_None' has invalid start frame 505. Video range is [0, 389].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_169'; source metadata written as null.

</details>