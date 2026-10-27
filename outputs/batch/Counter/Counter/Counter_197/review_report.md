# Play-Annotation-Generator Annotation Review — Counter_197

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_197`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | DE1 | defense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 152 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `22` | `21` | 153 | START | 153 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 157 | START | 157 | 170 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `18` | `17` | 157 | START | 157 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 157 | START | 157 | 176 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `20` | 157 | START | 157 | 237 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `3` | `2` | 157 | START | 157 | 237 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `15` | `14` | 168 | END | 153 | 168 |
| ✅ EXACT | `Action_Handoff` | DE1 | `15` | `14` | 180 | START | 180 | 194 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `8` | `7` | 195 | START | 195 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 237 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 198 | 46 | inferred_complete_timeline |
| `Action_None` | 204 | 277 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 223 | 71 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 232 | 80 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 157 | 237 | 81 | inferred_complete_timeline |
| `Action_None` | 238 | 244 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_SnapReceive` | 153 | 168 | 16 | inferred_complete_timeline |
| `Action_None` | 169 | 179 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 180 | 194 | 15 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 222 | 70 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 176 | 24 | inferred_complete_timeline |
| `Action_None` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 208 | 56 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_None` | 153 | 224 | 72 | inferred_complete_timeline |
| `Action_None` | 227 | 232 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–299 | 241 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–184 | 185 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–299 | 296 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–299 | 294 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–299 | 288 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 51–52 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 204–299 | 96 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 227–299 | 64 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 31 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [153-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-277] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-222] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-184] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-200] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-237] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '27' has 1 frames without a visible bounding box.
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