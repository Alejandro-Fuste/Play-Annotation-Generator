# Play-Annotation-Generator Annotation Review — RPO_254

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_254`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 79
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `28` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 13 | START | 13 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 13 | START | 13 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `1` | 63 | START | 63 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `10` | 63 | START | 63 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 63 | START | 63 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 63 | START | 63 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 63 | START | 63 | 72 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `6` | 72 | START | 72 | 105 |
| ✅ EXACT | `Action_PullBall` | QB | `6` | `6` | 106 | START | 106 | 113 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 141 | START | 141 | 145 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–157
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 71 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 72 | 105 | 34 | inferred_complete_timeline |
| `Action_PullBall` | 106 | 113 | 8 | inferred_complete_timeline |
| `Action_None` | 114 | 140 | 27 | inferred_complete_timeline |
| `Action_ThrowPass` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 157 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–157
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_None` | 71 | 91 | 21 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–92
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 81 | 20 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–79
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 79 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–157
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 145 | 83 | inferred_complete_timeline |
| `Action_None` | 146 | 157 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–120
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 120 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–159
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 79 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 145 | 27 | inferred_complete_timeline |
| `Action_None` | 146 | 159 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–156
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 145 | 39 | inferred_complete_timeline |
| `Action_None` | 146 | 156 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–135
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 135 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–158
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 114 | 53 | inferred_complete_timeline |
| `Action_None` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_None` | 130 | 158 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–160
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 157 | 96 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–150
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 144 | 83 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–151
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 151 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–162
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 62 | 162 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–154
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 59 | 47 | inferred_complete_timeline |
| `Action_None` | 74 | 154 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 51 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 24–47 | 9 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 99–158 | 60 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 131–150 | 20 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 138–157 | 14 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 174–239 | 63 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 177–218 | 36 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 206–213 | 8 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 27 | 51 | 21 | 84.0% | 28–31 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 51 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [13-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-158] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-144] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-91] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-81] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-120] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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