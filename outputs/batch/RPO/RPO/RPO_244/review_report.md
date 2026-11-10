# Play-Annotation-Generator Annotation Review — RPO_244

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_244`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `22` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_PullBall` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `15` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_RunBlock` | RT | `0` | `0` | 41 | START | 41 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `11` | `11` | 41 | START | 41 | 49 |
| ✅ EXACT | `Action_RunBlock` | LT | `3` | `3` | 41 | START | 41 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `6` | `6` | 41 | START | 41 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `8` | `8` | 41 | START | 41 | 66 |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | `15` | `14` | 56 | START | 56 | 66 |
| ✅ EXACT | `Action_PullBall` | Position_Unknown | `15` | `14` | 67 | START | 67 | 78 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `15` | `14` | 104 | START | 104 | 111 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 70 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 77 | 38 | inferred_complete_timeline |
| `Action_None` | 79 | 106 | 28 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 111 | 71 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 105 | 65 | inferred_complete_timeline |
| `Action_RunBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 111 | 42 | inferred_complete_timeline |
| `Action_None` | 112 | 136 | 25 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 66 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 82 | 111 | 30 | inferred_complete_timeline |
| `Action_None` | 112 | 141 | 30 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 111 | 71 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 108 | 69 | inferred_complete_timeline |
| `Action_None` | 114 | 136 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 149 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 87 | 48 | inferred_complete_timeline |
| `Action_None` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 82 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_None` | 54 | 65 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 70 | 31 | inferred_complete_timeline |
| `Action_None` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_None` | 89 | 210 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 165 | 126 | inferred_complete_timeline |
| `Action_None` | 168 | 181 | 14 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 45–132 | 70 | 8 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 54–95 | 16 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 79–210 | 115 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 100–179 | 69 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 107–210 | 22 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 114–166 | 49 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 122–150 | 29 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 136–210 | 75 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 148–178 | 27 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 170–210 | 41 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 175–210 | 35 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 192–210 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 66 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [112-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-105] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-82] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-55] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' for track '14' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ReadDefender' range [56-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [67-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '30' has 1 frames without a visible bounding box.
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

</details>