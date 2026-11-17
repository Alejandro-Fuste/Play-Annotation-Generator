# Play-Annotation-Generator Annotation Review — Power_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_94`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 20 | START | 20 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 20 | START | 20 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 20 | START | 20 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 20 | START | 20 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 20 | START | 20 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `16` | `Group` | 20 | START | 20 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 20 | START | 20 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 20 | START | 20 | 138 |
| ✅ EXACT | `Action_DownBlock` | LT | `1` | `1` | 139 | START | 139 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `10` | 139 | START | 139 | 153 |
| ✅ EXACT | `Action_DownBlock` | LG | `11` | `11` | 139 | START | 139 | 200 |
| ✅ EXACT | `Action_PullBlock` | RG | `9` | `9` | 139 | START | 139 | 200 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 20–209
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 209 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 20–252
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 110 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 204 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 252 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–253
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 58 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 83 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 230 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 253 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 20–250
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 200 | 62 | inferred_complete_timeline |
| `Action_None` | 201 | 250 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 20–213
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 200 | 62 | inferred_complete_timeline |
| `Action_None` | 201 | 213 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 20–214
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 153 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 172 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 177 | 200 | 24 | inferred_complete_timeline |
| `Action_None` | 201 | 214 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 20–247
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_PullBlock` | 139 | 200 | 62 | inferred_complete_timeline |
| `Action_None` | 201 | 234 | 34 | inferred_complete_timeline |
| `Action_None` | 237 | 247 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 176 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 239 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–218
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 47 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 172 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 218 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–198
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 198 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–211
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 164 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 211 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 226 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 329 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–312
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 220 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 297 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 312 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 20–264
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 80 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 204 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 246 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 264 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–208
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 208 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–307
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 125 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 307 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 69–250
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 69 | 250 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 20–57 | 37 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 150–329 | 171 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 183–270 | 87 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 187–329 | 132 | 4 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 206–241 | 36 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 229–329 | 101 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 232–329 | 89 | 2 | Undefined position; Undefined team |
| `24` | `40` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |
| `26` | `43` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 298–329 | 13 | 3 | Undefined position; Undefined team |
| `28` | `46` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 306–307 | 2 | 1 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 308–329 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-239] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-307] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-220] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-297] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-312] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-234] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-172] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [177-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-230] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-204] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-246] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-264] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-110] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-131] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-250] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-245] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-241] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-317] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-307] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-307] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>