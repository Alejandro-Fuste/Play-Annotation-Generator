# Play-Annotation-Generator Annotation Review — Counter_143

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_143`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 160 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 161 | START | 161 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `14` | `13` | 164 | START | 164 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 164 | START | 176 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 164 | START | 164 | 179 |
| ✅ EXACT | `Action_PullBlock` | RG | `8` | `7` | 164 | START | 164 | 246 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 164 | START | 164 | 229 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 175 | END | 161 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `18` | `17` | 197 | START | 197 | 236 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 246 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–319
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 175 | 15 | inferred_complete_timeline |
| `Action_None` | 176 | 196 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 236 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 307 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 314 | 319 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 235 | 75 | inferred_complete_timeline |
| `Action_None` | 243 | 306 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 164 | 229 | 66 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 232 | 234 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 189 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 269 | 18 | inferred_complete_timeline |
| `Action_None` | 272 | 311 | 40 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_None` | 317 | 327 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 201 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallSnap` | 161 | 175 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 189 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 246 | 83 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 251 | 91 | inferred_complete_timeline |
| `Action_None` | 269 | 274 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 327 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 194 | 34 | inferred_complete_timeline |
| `Action_None` | 208 | 329 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 211 | 51 | inferred_complete_timeline |
| `Action_None` | 214 | 329 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 226 | 66 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 246 | 86 | inferred_complete_timeline |
| `Action_None` | 249 | 273 | 25 | inferred_complete_timeline |
| `Action_None` | 278 | 311 | 34 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 279 | 119 | inferred_complete_timeline |
| `Action_None` | 281 | 329 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 281 | 121 | inferred_complete_timeline |
| `Action_None` | 285 | 300 | 16 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 329 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 227 | 67 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_None` | 235 | 257 | 23 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 221–329 | 107 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 248–329 | 81 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 251–329 | 73 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 252–254 | 3 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 274–301 | 17 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 274–286 | 13 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 284–329 | 32 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `22`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [161–175], lower_priority='Action_DownBlock' annotated_start=164, effective_Action_DownBlock_start=176.
- ⚠️ Action 'Action_None' range [161-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [164-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [232-234] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-329] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-246] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-273] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-311] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-300] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-279] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [203-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-327] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-257] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [314-319] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [176-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-201] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [204-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-214] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [225-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-286] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '30' has 1 frames without a visible bounding box.
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

</details>