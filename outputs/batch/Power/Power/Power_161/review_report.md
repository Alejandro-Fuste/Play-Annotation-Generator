# Play-Annotation-Generator Annotation Review — Power_161

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_161`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `24` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_DownBlock` | DE1 | defense | `5` | `5` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 22 | START | 22 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 22 | START | 22 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 22 | START | 22 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 22 | START | 22 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 22 | START | 22 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 22 | START | 22 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 22 | START | 22 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 22 | START | 22 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 22 | START | 22 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `24` | `Group` | 22 | START | 124 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `17` | 144 | START | 144 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `19` | 144 | START | 144 | 152 |
| ✅ EXACT | `Action_DownBlock` | DE1 | `5` | `5` | 144 | START | 144 | 209 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `18` | 144 | START | 144 | 209 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 124–299
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 124 | 138 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 280 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 228 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 172 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 251 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 270 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 283 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 22–159
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 159 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 22–297
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 152 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 196 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_None` | 210 | 276 | 67 | inferred_complete_timeline |
| `Action_None` | 278 | 297 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 172 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 209 | 15 | inferred_complete_timeline |
| `Action_None` | 210 | 267 | 58 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 209 | 66 | inferred_complete_timeline |
| `Action_None` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 22–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 207 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 22–293
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 143 | 122 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 209 | 66 | inferred_complete_timeline |
| `Action_None` | 210 | 290 | 81 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 199 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–203
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 177 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 202 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 219 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 294 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 246 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 299 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 22–280
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 280 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 299 | 278 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 22–299 | 246 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 38–117 | 23 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 106–299 | 59 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 161–299 | 133 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 243–299 | 56 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 286–297 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 324: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [22-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-283] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-186] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-290] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-280] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-294] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-299] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-172] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [180-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-267] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-209] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-207] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-141] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-257] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-280] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-216] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-228] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>