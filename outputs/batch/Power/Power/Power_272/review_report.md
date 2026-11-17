# Play-Annotation-Generator Annotation Review — Power_272

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_272`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 80
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 0
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `16` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 19 | START | 19 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 19 | START | 19 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 19 | START | 19 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 19 | START | 19 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 19 | START | 19 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `0` | `0` | 105 | START | 105 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `11` | `11` | 105 | START | 105 | 116 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `16` | `15` | 105 | START | 159 | 191 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 19–143
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 143 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 104 | 86 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 118 | 146 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 167 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_None` | 192 | 269 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 19–155
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 111 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 141 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 155 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 19–131
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 131 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 19–106
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 106 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 202 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 19–190
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 190 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 134 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 169 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 224 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 260 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 186 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 269 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 19–146 | 126 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 19–269 | 248 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 19–190 | 172 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 19–269 | 247 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 21–177 | 157 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 50–269 | 115 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 104–269 | 151 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 116–269 | 134 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 126–156 | 9 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 129–269 | 122 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 135–269 | 128 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 165–269 | 80 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 170–269 | 90 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 176–269 | 94 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 176–269 | 92 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 209–269 | 59 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 219–224 | 4 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 228–231 | 4 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 259–261 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | 20 | 84 | 40 | 61.5% | 56–80 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (5 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `16` (Position_Unknown): Annotated start 105 != Inferred start 159

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 543: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 544: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '13' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [105-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-146] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-202] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-207] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-135] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-131] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [118-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-175] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-177] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-55] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-245] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-202] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>