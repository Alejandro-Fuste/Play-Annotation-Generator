# Play-Annotation-Generator Annotation Review — Counter_367

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_367`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 182 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `14` | `13` | 183 | START | 183 | 196 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `17` | `16` | 186 | START | 186 | 209 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 186 | START | 186 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 186 | START | 186 | 222 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `10` | `9` | 186 | START | 186 | 248 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 196 | END | 183 | 196 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 205 | START | 205 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `21` | `20` | 222 | START | 222 | 250 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 261 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_SnapReceive` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 205 | 221 | 17 | inferred_complete_timeline |
| `Action_None` | 222 | 329 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 114 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 206 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 221 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 250 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 273 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 286 | 290 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 292 | 329 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 186 | 248 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 201 | 19 | inferred_complete_timeline |
| `Action_None` | 207 | 252 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 195 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 207 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 237 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 254 | 261 | 8 | inferred_complete_timeline |
| `Action_None` | 262 | 271 | 10 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 234 | 52 | inferred_complete_timeline |
| `Action_None` | 237 | 256 | 20 | inferred_complete_timeline |
| `Action_None` | 260 | 305 | 46 | inferred_complete_timeline |
| `Action_None` | 308 | 319 | 12 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 222 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 227 | 261 | 35 | inferred_complete_timeline |
| `Action_None` | 262 | 329 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 219 | 37 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 233 | 250 | 18 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 258 | 76 | inferred_complete_timeline |
| `Action_None` | 261 | 329 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 226 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 209 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 305 | 123 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 319 | 137 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_BallSnap` | 183 | 196 | 14 | inferred_complete_timeline |
| `Action_None` | 197 | 329 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 305 | 123 | inferred_complete_timeline |
| `Action_None` | 309 | 329 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 275 | 93 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 29–35 | 7 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 65–125 | 25 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 216–224 | 8 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 231–329 | 60 | 10 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 233–235 | 3 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 236–316 | 46 | 7 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 278–329 | 35 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 293–311 | 11 | 4 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 296–329 | 34 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 316–318 | 3 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [183-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-252] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-319] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [186-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-305] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-226] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-256] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-305] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [286-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-96] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-275] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-300] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-290] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '34' has 1 frames without a visible bounding box.
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

</details>