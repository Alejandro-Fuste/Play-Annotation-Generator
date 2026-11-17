# Play-Annotation-Generator Annotation Review — Power_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_164`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 0
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `15` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `17` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 30 | START | 30 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 30 | START | 30 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 30 | START | 30 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 30 | START | 30 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `15` | `13` | 181 | START | 181 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `5` | 181 | START | 181 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `17` | `15` | 181 | START | 181 | 192 |

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
- **Visible Frames:** 30–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 266 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 30–291
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 210 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 261 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 291 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 30–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 236 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 256 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 329 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 30–279
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 180 | 151 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 193 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 226 | 12 | inferred_complete_timeline |
| `Action_None` | 227 | 279 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 30–307
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 276 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 307 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 30–200
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 186 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 30–288
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 190 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 233 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 288 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 30–329
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 173 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 194 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 329 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 30–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 180 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 30–225
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 177 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 193 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 225 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 30–193
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 188 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 193 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 30–222 | 181 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 51–60 | 10 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 170–329 | 70 | 7 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 179–190 | 12 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 181–204 | 18 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 196–329 | 102 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 204–329 | 104 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 204–329 | 123 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 214–262 | 49 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 223–319 | 84 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 229–329 | 79 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 232–310 | 70 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 233–309 | 48 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 259–329 | 71 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 304–306 | 3 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 309–310 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 310–329 | 20 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 311–329 | 14 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 313–326 | 14 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 321–329 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 330: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 330: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 330: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [30-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-291] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-207] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-233] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-60] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [217-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [181-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [199-204] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-231] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-262] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-254] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-319] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-277] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-288] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-310] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-309] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-326] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>