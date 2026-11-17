# Play-Annotation-Generator Annotation Review — Power_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_85`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 16 | START | 16 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 16 | START | 16 | 294 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 16 | START | 16 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 16 | START | 16 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 16 | START | 16 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 16 | START | 16 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 16 | START | 16 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 16 | START | 16 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 16 | START | 16 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 16 | START | 16 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 16 | START | 16 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `17` | 175 | START | 175 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 175 | START | 175 | 197 |
| ✅ EXACT | `Action_PullBlock` | RG | `16` | `16` | 175 | START | 175 | 217 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 299 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–207
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 207 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 299 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 16–294
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 294 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 299 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–297
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 242 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 276 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 297 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 220 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 16–299
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 174 | 159 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 208 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 212 | 218 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_None` | 273 | 288 | 16 | inferred_complete_timeline |
| `Action_None` | 290 | 294 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–208
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 174 | 159 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 197 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 208 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 16–266
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 174 | 159 | inferred_complete_timeline |
| `Action_PullBlock` | 175 | 217 | 43 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 237 | 8 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 255 | 266 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 16–294
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 221 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 268 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 288 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 294 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 195 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 243 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 269 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 299 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 235 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 250 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 266 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 275 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 288 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 193 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 288 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 16–216
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 216 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 226 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 239 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 294 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 164 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 184 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–262
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 210 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 258 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–297
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 294 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–294
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 288 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 294 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–250
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 250 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–294
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 270 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 294 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 29–116 | 23 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 209–291 | 72 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 261–288 | 17 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 264–294 | 30 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 283–292 | 10 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 291–294 | 4 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 104 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [16-294] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-207] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-258] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-242] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-297] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-294] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-216] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-221] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-268] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-288] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [175-217] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-237] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-266] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-208] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [212-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-193] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-220] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-220] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-250] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-266] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-275] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-195] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-243] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-116] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-237] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-266] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-288] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-266] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-294] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-292] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-294] for track '27' has 1 frames without a visible bounding box.
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

</details>