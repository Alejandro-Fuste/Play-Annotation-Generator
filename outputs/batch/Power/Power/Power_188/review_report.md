# Play-Annotation-Generator Annotation Review — Power_188

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_188`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 24
- **Ball Tracks:** 2
- **Action Segments:** 59
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 23
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE2 | offense | `11` | `11` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 11 | START | 11 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 11 | START | 11 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 11 | START | 21 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 11 | START | 41 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 11 | START | 11 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 11 | START | 11 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 11 | START | 11 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 11 | START | 11 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 11 | START | 11 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE2 | `11` | `11` | 194 | START | 194 | 202 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `13` | `13` | 194 | START | 194 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `3` | `3` | 194 | START | 194 | 202 |
| ✅ EXACT | `Action_PullBlock` | RG | `2` | `2` | 194 | START | 194 | 222 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 21–229
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 109 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 140 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 168 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 182 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 211 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 229 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–297
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 297 | 287 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 225 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–288
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 193 | 183 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 245 | 42 | inferred_complete_timeline |
| `Action_None` | 246 | 288 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 11–220
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 220 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–266
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 193 | 183 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 245 | 27 | inferred_complete_timeline |
| `Action_None` | 246 | 266 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 41–262
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 188 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 202 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–222
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 193 | 183 | inferred_complete_timeline |
| `Action_PullBlock` | 194 | 222 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–259
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 212 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 259 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–321
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 321 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 11–260
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 193 | 183 | inferred_complete_timeline |
| `Action_DownBlock` | 194 | 245 | 52 | inferred_complete_timeline |
| `Action_None` | 246 | 260 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–257
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 257 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 244 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 329 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 269 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 329 | 319 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 48–207 | 138 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 58–329 | 272 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 151–236 | 86 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 204–329 | 125 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 215–312 | 95 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 227–329 | 103 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 306–329 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | 11 | 31 | 21 | 100.0% | None |
| `19` | `20` | 198 | 198 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 47 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [11-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [194-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [219-245] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-212] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-259] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-321] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [194-202] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-245] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-109] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-168] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-211] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-229] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-52] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-130] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-178] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-202] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-236] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-326] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-312] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>