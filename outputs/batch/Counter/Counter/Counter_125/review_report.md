# Play-Annotation-Generator Annotation Review — Counter_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_125`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 142 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 143 | START | 143 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `13` | `12` | 144 | START | 144 | 227 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `15` | `14` | 148 | START | 157 | 234 |
| ✅ EXACT | `Action_DownBlock` | LG | `21` | `20` | 148 | START | 148 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 148 | START | 148 | 193 |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | `3` | `2` | 148 | START | 148 | 234 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 156 | END | 143 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 181 | START | 181 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 234 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_SnapReceive` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_None` | 157 | 180 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 235 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 246 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 260 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 262 | 329 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 144 | 227 | 84 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 230 | 287 | 58 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 148 | 234 | 87 | inferred_complete_timeline |
| `Action_None` | 235 | 329 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 235 | 93 | inferred_complete_timeline |
| `Action_None` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 329 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 183 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_BallSnap` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 234 | 78 | inferred_complete_timeline |
| `Action_None` | 235 | 329 | 95 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 193 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 198 | 234 | 37 | inferred_complete_timeline |
| `Action_None` | 235 | 329 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 198 | 56 | inferred_complete_timeline |
| `Action_None` | 201 | 289 | 89 | inferred_complete_timeline |
| `Action_None` | 293 | 307 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 224 | 82 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 248 | 106 | inferred_complete_timeline |
| `Action_None` | 250 | 284 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 290 | 148 | inferred_complete_timeline |
| `Action_None` | 303 | 329 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 230 | 88 | inferred_complete_timeline |
| `Action_None` | 235 | 283 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 329 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 295 | 153 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_None` | 143 | 287 | 145 | inferred_complete_timeline |
| `Action_None` | 289 | 301 | 13 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 85–100 | 16 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 126–138 | 6 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 169–304 | 77 | 7 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 196–201 | 6 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 196–329 | 111 | 11 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 225–255 | 30 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 248–298 | 39 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 250–329 | 79 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 257–329 | 58 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 263–329 | 67 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 267–270 | 4 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 277–295 | 16 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 291–329 | 37 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 300–329 | 30 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 307–329 | 23 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `13` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (C): Annotated start 148 != Inferred start 157
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [143–156], lower_priority='Action_DownBlock' annotated_start=148, effective_Action_DownBlock_start=157.
- ⚠️ Action 'Action_None' range [143-224] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-283] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-248] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-295] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-287] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-301] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [144-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [230-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-290] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-183] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-273] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-316] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-282] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-271] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-298] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-316] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '37' has 1 frames without a visible bounding box.
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