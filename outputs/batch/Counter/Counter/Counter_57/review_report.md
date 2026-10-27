# Play-Annotation-Generator Annotation Review — Counter_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_57`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 172 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 173 | START | 173 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 174 | START | 174 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `3` | 174 | START | 174 | 203 |
| ✅ EXACT | `Action_PullBlock` | RG | `15` | `14` | 174 | START | 174 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `2` | `1` | 174 | START | 174 | 254 |
| ✅ EXACT | `Action_SnapReceive` | RB | `19` | `18` | 192 | END | 173 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `19` | `18` | 217 | START | 217 | 280 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 266 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_SnapReceive` | 173 | 192 | 20 | inferred_complete_timeline |
| `Action_None` | 193 | 216 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 280 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 290 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 303 | 317 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 328 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 290 | 118 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 316 | 144 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 174 | 254 | 81 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 259 | 266 | 8 | inferred_complete_timeline |
| `Action_None` | 267 | 329 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 203 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 221 | 266 | 46 | inferred_complete_timeline |
| `Action_None` | 267 | 326 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 135 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 162 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 173 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 215 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 266 | 41 | inferred_complete_timeline |
| `Action_None` | 267 | 289 | 23 | inferred_complete_timeline |
| `Action_None` | 292 | 294 | 3 | inferred_complete_timeline |
| `Action_None` | 302 | 313 | 12 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_BallSnap` | 173 | 187 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 231 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 214 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 236 | 64 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 271 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 321 | 149 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 195 | 23 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 296 | 87 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 321 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 229 | 243 | 15 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 273 | 18 | inferred_complete_timeline |
| `Action_None` | 275 | 280 | 6 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 273 | 101 | inferred_complete_timeline |
| `Action_None` | 282 | 329 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 216 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 304 | 132 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–310 | 287 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 9–12 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 211–215 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 222–280 | 59 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 237–329 | 67 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 246–329 | 83 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 252–329 | 67 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 285–299 | 4 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 295–302 | 8 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 116: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 93 frames exceeds threshold 90 frames [start=174, end=266].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LG) duration 93 frames exceeds threshold 90 frames [start=174, end=266].
- ⚠️ Action 'Action_None' range [173-290] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [174-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-203] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-326] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-291] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-321] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-321] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [173-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-290] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-293] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-317] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-328] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-214] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-273] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-135] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-162] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-182] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-289] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-313] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-278] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-280] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-329] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-302] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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