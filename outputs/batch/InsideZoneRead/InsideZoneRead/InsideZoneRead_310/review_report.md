# Play-Annotation-Generator Annotation Review — InsideZoneRead_310

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_310`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `20` | `17` |
| ✅ EXACT | `Action_Keep` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 14 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `16` | 15 | START | 63 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 18 | START | 18 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 18 | START | 18 | 77 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 18 | START | 18 | 31 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 18 | START | 18 | 111 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `16` | `15` | 34 | END | 15 | 34 |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | `16` | `15` | 39 | START | 39 | 45 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | `20` | `17` | 44 | START | 65 | 111 |
| ✅ EXACT | `Action_Keep` | Position_Unknown | `16` | `15` | 46 | START | 46 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 70 | START | 70 | 75 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 58 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 64 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 85 | 17 | inferred_complete_timeline |
| `Action_None` | 108 | 210 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 77 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 111 | 32 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 31 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 105 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 78 | 64 | inferred_complete_timeline |
| `Action_None` | 80 | 108 | 29 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 44 | 30 | inferred_complete_timeline |
| `Action_None` | 46 | 94 | 49 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 58 | 44 | inferred_complete_timeline |
| `Action_None` | 65 | 210 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 96 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 129 | 115 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 95 | 81 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 10–210 | 197 | 7 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 63–210 | 147 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 65–208 | 143 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 76–181 | 106 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 81–97 | 17 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 104–210 | 100 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 104–210 | 92 | 5 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 105–210 | 106 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 134–210 | 74 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 136–210 | 75 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 144–177 | 34 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 155–175 | 7 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 156–162 | 7 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 192–210 | 18 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 192–197 | 5 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 15 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `20` (Position_Unknown): Annotated start 44 != Inferred start 65
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=63, end=34. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-78] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-94] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-33] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-31] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-64] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [15-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-181] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-178] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-153] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-177] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_310'; source metadata written as null.

</details>