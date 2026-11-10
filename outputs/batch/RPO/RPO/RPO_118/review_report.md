# Play-Annotation-Generator Annotation Review — RPO_118

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_118`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `33` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `10` | `10` | 62 | START | 62 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `11` | `11` | 62 | START | 62 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `14` | `14` | 62 | START | 62 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `3` | `3` | 62 | START | 62 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `4` | `4` | 62 | START | 62 | 68 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `8` | 66 | START | 66 | 74 |
| ✅ EXACT | `Action_PullBall` | QB | `8` | `8` | 75 | START | 75 | 83 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 122 | START | 122 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 65 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 75 | 83 | 9 | inferred_complete_timeline |
| `Action_None` | 84 | 121 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 122 | 129 | 8 | inferred_complete_timeline |
| `Action_None` | 130 | 146 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 84 | 24 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 128 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 84 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 30 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 94 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 103 | 129 | 27 | inferred_complete_timeline |
| `Action_None` | 130 | 144 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 92 | 107 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 120 | 7 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 71 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 75 | 89 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 129 | 8 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 62 | 81 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 85 | 129 | 45 | inferred_complete_timeline |
| `Action_None` | 130 | 149 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 115 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 78 | 18 | inferred_complete_timeline |
| `Action_None` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_None` | 106 | 142 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 139 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 151 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 136 | 76 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 103 | 43 | inferred_complete_timeline |
| `Action_None` | 107 | 147 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 107 | 47 | inferred_complete_timeline |
| `Action_None` | 138 | 179 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 100–155 | 51 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 110–139 | 30 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 113–142 | 30 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 140–145 | 6 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 147–180 | 34 | 1 | Undefined position; Undefined team |
| `20` | `33` | Position_Unknown | Team_Unknown | 154–180 | 27 | 1 | Undefined position; Undefined team |
| `21` | `34` | Position_Unknown | Team_Unknown | 154–176 | 9 | 2 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 155–180 | 26 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 167–172 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 50 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [61-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [75-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [96-105] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [71-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [92-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-120] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [75-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-142] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [79-84] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [85-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [62-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-142] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '23' has 1 frames without a visible bounding box.
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

</details>