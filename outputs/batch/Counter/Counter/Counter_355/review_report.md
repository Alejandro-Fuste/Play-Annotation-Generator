# Play-Annotation-Generator Annotation Review — Counter_355

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_355`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 154 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 155 | START | 155 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 158 | START | 174 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 158 | START | 158 | 184 |
| ✅ EXACT | `Action_DownBlock` | RT | `8` | `7` | 158 | START | 158 | 236 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `11` | `10` | 158 | START | 158 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 158 | START | 158 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 170 | END | 155 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 179 | START | 179 | 197 |
| ✅ EXACT | `Action_BallCarry` | RB | `21` | `20` | 198 | START | 198 | 222 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 236 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_SnapReceive` | 155 | 170 | 16 | inferred_complete_timeline |
| `Action_None` | 171 | 178 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 179 | 197 | 19 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 197 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 222 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 329 | 175 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 329 | 175 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 329 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 158 | 210 | 53 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 221 | 236 | 16 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 329 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PullBlock` | 158 | 198 | 41 | inferred_complete_timeline |
| `Action_PullBlock` | 202 | 236 | 35 | inferred_complete_timeline |
| `Action_None` | 237 | 246 | 10 | inferred_complete_timeline |
| `Action_None` | 251 | 299 | 49 | inferred_complete_timeline |
| `Action_None` | 301 | 307 | 7 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_BallSnap` | 155 | 170 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 236 | 58 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 157 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 184 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 191 | 236 | 46 | inferred_complete_timeline |
| `Action_None` | 237 | 237 | 1 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_DownBlock` | 158 | 236 | 79 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 296 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 216 | 62 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 258 | 34 | inferred_complete_timeline |
| `Action_None` | 261 | 266 | 6 | inferred_complete_timeline |
| `Action_None` | 273 | 329 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 273 | 119 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 195 | 41 | inferred_complete_timeline |
| `Action_None` | 212 | 227 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 191 | 37 | inferred_complete_timeline |
| `Action_None` | 193 | 278 | 86 | inferred_complete_timeline |
| `Action_None` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 223 | 69 | inferred_complete_timeline |
| `Action_None` | 231 | 310 | 80 | inferred_complete_timeline |
| `Action_None` | 312 | 329 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 327 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 300 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 329 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_None` | 155 | 266 | 112 | inferred_complete_timeline |
| `Action_None` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–307 | 298 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 226–329 | 91 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 231–329 | 99 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 293–329 | 37 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 308–329 | 9 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 313–329 | 16 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [155–170], lower_priority='Action_DownBlock' annotated_start=158, effective_Action_DownBlock_start=171.
- ⚠️ Action 'Action_None' range [155-216] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [158-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-299] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-296] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-271] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-301] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [155-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-157] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [158-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [191-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 237, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [237-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-244] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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