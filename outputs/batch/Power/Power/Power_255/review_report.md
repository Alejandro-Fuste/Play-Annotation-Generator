# Play-Annotation-Generator Annotation Review — Power_255

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_255`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 109
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
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 10 | START | 10 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 10 | START | 10 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 10 | START | 10 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 10 | START | 10 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 10 | START | 10 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 10 | START | 16 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 10 | START | 20 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 10 | START | 10 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 10 | START | 10 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `19` | `19` | 136 | START | 136 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `20` | `20` | 136 | START | 136 | 151 |
| ✅ EXACT | `Action_DownBlock` | RG | `21` | `21` | 136 | START | 136 | 166 |
| ✅ EXACT | `Action_PullBlock` | LG | `14` | `14` | 136 | START | 136 | 234 |

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
- **Visible Frames:** 10–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 258 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 10–188
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 177 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 188 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 10–258
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 181 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 197 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 258 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 269 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 147 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 192 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 228 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 265 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 135 | 126 | inferred_complete_timeline |
| `Action_PullBlock` | 136 | 234 | 99 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 135 | 126 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 192 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 219 | 234 | 16 | inferred_complete_timeline |
| `Action_None` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 20–166
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 135 | 116 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 166 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–189
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 135 | 120 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 189 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 218 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 265 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–192
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 169 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 192 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–154
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 154 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 156 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 202 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 265 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 232 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–223
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 209 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 223 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 269 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 235 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 248 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 269 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 10–192
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 181 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 192 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 10–269 | 260 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 10–269 | 260 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 169–203 | 35 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 195–269 | 68 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 202–269 | 67 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 206–269 | 64 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 208–269 | 22 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 212–224 | 13 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 217–264 | 44 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 236–269 | 30 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 237–269 | 31 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 239–265 | 21 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 239–253 | 15 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 245–269 | 20 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 247–269 | 14 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 256–269 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 509: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 510: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (LG) duration 99 frames exceeds threshold 90 frames [start=136, end=234].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (C) duration 99 frames exceeds threshold 90 frames [start=136, end=234].
- ⚠️ Action 'Action_PreSnap' range [10-235] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-197] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-258] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-258] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-209] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-265] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-202] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-265] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-218] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-265] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-203] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-218] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-258] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-265] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-254] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-253] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-253] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-264] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-252] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>