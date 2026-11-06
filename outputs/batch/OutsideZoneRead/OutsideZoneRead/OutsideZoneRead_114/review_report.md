# Play-Annotation-Generator Annotation Review — OutsideZoneRead_114

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_114`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 20 | START | 20 | 32 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 23 | START | 23 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 23 | START | 23 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 23 | START | 40 | 42 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 23 | START | 23 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 23 | START | 23 | 44 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 33 | END | 20 | 33 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `10` | 37 | START | 37 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `11` | `10` | 47 | START | 47 | 58 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `3` | `2` | 59 | START | 59 | 86 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 66 | START | 66 | 104 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 33 | 14 | inferred_complete_timeline |
| `Action_None` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_Keep` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_Keep` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 104 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 129 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 107 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 62 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_None` | 87 | 107 | 21 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 86 | 64 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 32 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 86 | 30 | inferred_complete_timeline |
| `Action_None` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 58 | 36 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_None` | 87 | 183 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 86 | 39 | inferred_complete_timeline |
| `Action_None` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 141 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 97 | 78 | inferred_complete_timeline |
| `Action_None` | 100 | 162 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 121 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 113 | 94 | inferred_complete_timeline |
| `Action_None` | 115 | 210 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 192 | 173 | inferred_complete_timeline |
| `Action_None` | 194 | 210 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `19` | Position_Unknown | Team_Unknown | 76–210 | 92 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 82–210 | 129 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 82–84 | 3 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 90–209 | 116 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 142–172 | 28 | 3 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 155–210 | 52 | 4 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `25` | `41` | Position_Unknown | Team_Unknown | 187–189 | 3 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [20–33], lower_priority='Action_ZoneBlock' annotated_start=23, effective_Action_ZoneBlock_start=34.
- ⚠️ Action 'Action_None' range [20-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-162] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-113] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [47-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-62] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [20-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '27' has 3 frames without a visible bounding box.
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

</details>