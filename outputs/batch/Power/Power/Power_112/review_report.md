# Play-Annotation-Generator Annotation Review — Power_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_112`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 54
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 32
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 13 | START | 13 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 13 | START | 13 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 13 | START | 13 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 13 | START | 13 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 13 | START | 13 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 13 | START | 13 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 13 | START | 13 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 13 | START | 13 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `10` | `10` | 190 | START | 190 | 234 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `7` | `7` | 190 | START | 190 | 223 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `8` | `8` | 190 | START | 190 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `9` | `9` | 190 | START | 190 | 198 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 329 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 52 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 232 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 258 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 239 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 329 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 199 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 234 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–312
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 189 | 177 | inferred_complete_timeline |
| `Action_PullBlock` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 212 | 218 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 247 | 28 | inferred_complete_timeline |
| `Action_None` | 248 | 308 | 61 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–253
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 189 | 177 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 211 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 247 | 18 | inferred_complete_timeline |
| `Action_None` | 248 | 253 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 230 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 329 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 189 | 177 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 234 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 247 | 12 | inferred_complete_timeline |
| `Action_None` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_None` | 262 | 329 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 81–329
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 81 | 148 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 226 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 329 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–223
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 189 | 177 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 223 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–227
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 227 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 303 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 329 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 13–329 | 317 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 13–70 | 58 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 215–329 | 115 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 219–329 | 107 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 221–224 | 4 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 222–329 | 108 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 235–329 | 95 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 236–329 | 91 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 249–329 | 81 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 263–329 | 67 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 270–329 | 60 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 278–329 | 52 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | 35 | 44 | 6 | 60.0% | 36, 41–43 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 32 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [13-303] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-234] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-239] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [190-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [201-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [212-218] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-308] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-234] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-263] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-329] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>