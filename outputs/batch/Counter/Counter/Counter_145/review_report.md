# Play-Annotation-Generator Annotation Review — Counter_145

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_145`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 151 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 150 | START | 150 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 151 | END | 150 | 151 |
| ✅ EXACT | `Action_DownBlock` | QB | `10` | `9` | 152 | START | 152 | 176 |
| ✅ EXACT | `Action_DownBlock` | RT | `18` | `17` | 152 | START | 152 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 152 | START | 152 | 160 |
| ✅ EXACT | `Action_PullBlock` | LG | `8` | `7` | 152 | START | 152 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `17` | `16` | 152 | START | 152 | 228 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 177 | START | 177 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 188 | START | 188 | 213 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_SnapReceive` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 176 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 177 | 187 | 11 | inferred_complete_timeline |
| `Action_None` | 188 | 329 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 213 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 236 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 311 | 74 | inferred_complete_timeline |
| `Action_BallCarry` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 280 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 233 | 84 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 304 | 67 | inferred_complete_timeline |
| `Action_None` | 306 | 310 | 5 | inferred_complete_timeline |
| `Action_None` | 312 | 329 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 199 | 50 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 236 | 31 | inferred_complete_timeline |
| `Action_None` | 238 | 277 | 40 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |
| `Action_None` | 283 | 303 | 21 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 326 | 5 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 152 | 228 | 77 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 259 | 19 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 314 | 34 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PullBlock` | 152 | 233 | 82 | inferred_complete_timeline |
| `Action_None` | 234 | 313 | 80 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_BallSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 160 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 198 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 233 | 33 | inferred_complete_timeline |
| `Action_None` | 234 | 250 | 17 | inferred_complete_timeline |
| `Action_None` | 262 | 264 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 171 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 177 | 28 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |
| `Action_None` | 214 | 220 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 176 | 27 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 228 | 278 | 51 | inferred_complete_timeline |
| `Action_None` | 280 | 304 | 25 | inferred_complete_timeline |
| `Action_None` | 306 | 325 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 149 | 72 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 181 | 13 | inferred_complete_timeline |
| `Action_None` | 183 | 260 | 78 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 312 | 38 | inferred_complete_timeline |
| `Action_None` | 316 | 320 | 5 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_None` | 150 | 160 | 11 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 200 | 34 | inferred_complete_timeline |
| `Action_None` | 203 | 211 | 9 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 206 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 195 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 230 | 81 | inferred_complete_timeline |
| `Action_None` | 256 | 270 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 280 | 131 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 245 | 96 | inferred_complete_timeline |
| `Action_None` | 247 | 266 | 20 | inferred_complete_timeline |
| `Action_None` | 268 | 274 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_None` | 150 | 158 | 9 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 149–329 | 174 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 212–311 | 94 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 220–310 | 76 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 225–311 | 87 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 240–262 | 21 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 243–317 | 75 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 256–329 | 72 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 289–329 | 38 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 306–329 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 292: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [150-177] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-304] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-325] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-311] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-176] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-313] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [177-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-233] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-304] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-329] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-260] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-312] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-199] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-236] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-277] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-303] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-326] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [152-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 234, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [234-236] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-314] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-158] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-233] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-250] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-204] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-329] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-302] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-311] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-262] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-317] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-311] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '29' has 1 frames without a visible bounding box.
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

</details>