# Play-Annotation-Generator Annotation Review — InsideZoneRead_332

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_332`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `28` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | offense | `18` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `16` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `20` | `16` |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | Team_Unknown | `20` | `16` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 30 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `28` | `19` | 28 | START | 152 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 31 | START | 31 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `13` | 31 | START | 31 | 95 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | `18` | `15` | 31 | START | 99 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 31 | START | 31 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 31 | START | 31 | 95 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `20` | `16` | 40 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `20` | `16` | 45 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Keep` | Position_Unknown | `20` | `16` | 48 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `20` | `16` | 67 | START | 121 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 95 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 205 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 109 | 82 | inferred_complete_timeline |
| `Action_None` | 112 | 192 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 239 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 95 | 65 | inferred_complete_timeline |
| `Action_None` | 96 | 122 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 95 | 65 | inferred_complete_timeline |
| `Action_None` | 96 | 169 | 74 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 95 | 65 | inferred_complete_timeline |
| `Action_None` | 96 | 162 | 67 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 95 | 65 | inferred_complete_timeline |
| `Action_None` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_None` | 111 | 162 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 99–224
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 99 | 99 | 1 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 224 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 239 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 146 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 116 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 188 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 178 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 229 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–174 | 167 | 5 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 91–167 | 15 | 4 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 121–239 | 119 | 1 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 131–180 | 50 | 1 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 146–166 | 21 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 152–169 | 18 | 2 | Undefined position; Undefined team |
| `20` | `32` | Position_Unknown | Team_Unknown | 173–189 | 17 | 1 | Undefined position; Undefined team |
| `21` | `33` | Position_Unknown | Team_Unknown | 179–239 | 61 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 183–239 | 56 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `28` (Position_Unknown): Annotated start 28 != Inferred start 152
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (RT): Annotated start 31 != Inferred start 99
- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_Keep` on target `20` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `20` (Position_Unknown): Annotated start 67 != Inferred start 121

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=99, end=95. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '16' has invalid range: start=121, end=40. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '16' has invalid range: start=121, end=47. Clamping end to start.
- ⚠️ Segment 'Action_Keep' for track '16' has invalid range: start=121, end=66. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=152, end=40. Clamping end to start.
- ⚠️ Action 'Action_None' range [28-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-229] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-146] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-146] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-169] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-122] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_332'; source metadata written as null.

</details>