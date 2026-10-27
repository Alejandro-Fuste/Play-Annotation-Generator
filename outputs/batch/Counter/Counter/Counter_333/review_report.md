# Play-Annotation-Generator Annotation Review — Counter_333

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_333`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 193 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 144 | START | 144 | 160 |
| ✅ EXACT | `Action_DownBlock` | LG | `11` | `10` | 147 | START | 147 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `18` | `17` | 147 | START | 147 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 147 | START | 147 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `21` | `20` | 147 | START | 165 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `3` | `2` | 147 | START | 147 | 221 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 160 | END | 144 | 160 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 174 | START | 174 | 193 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 194 | START | 194 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 243 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_SnapReceive` | 144 | 160 | 17 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 193 | 20 | inferred_complete_timeline |
| `Action_None` | 194 | 329 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 329 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 147 | 221 | 75 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 224 | 243 | 20 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 258 | 329 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 187 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_BallSnap` | 144 | 160 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 244 | 259 | 16 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 271 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 195 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 233 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 250 | 7 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 171 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 196 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 243 | 43 | inferred_complete_timeline |
| `Action_None` | 244 | 265 | 22 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 259 | 116 | inferred_complete_timeline |
| `Action_None` | 261 | 321 | 61 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 175 | 32 | inferred_complete_timeline |
| `Action_None` | 177 | 181 | 5 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 208 | 15 | inferred_complete_timeline |
| `Action_None` | 210 | 311 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 177 | 34 | inferred_complete_timeline |
| `Action_None` | 180 | 216 | 37 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 179 | 36 | inferred_complete_timeline |
| `Action_None` | 188 | 329 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 225 | 82 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 244 | 101 | inferred_complete_timeline |
| `Action_None` | 246 | 254 | 9 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 242 | 99 | inferred_complete_timeline |
| `Action_None` | 244 | 321 | 78 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 329 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 144 | 1 | inferred_complete_timeline |
| `Action_None` | 156 | 268 | 113 | inferred_complete_timeline |
| `Action_None` | 271 | 309 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_None` | 144 | 286 | 143 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–329 | 324 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 81–90 | 10 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 158–164 | 7 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 173–250 | 11 | 3 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 175–221 | 40 | 3 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 213–329 | 102 | 5 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 233–329 | 92 | 2 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 253–329 | 77 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 267–324 | 43 | 3 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 273–329 | 54 | 2 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 275–329 | 55 | 1 | Undefined position; Undefined team |
| `34` | `58` | Position_Unknown | Team_Unknown | 307–329 | 23 | 1 | Undefined position; Undefined team |
| `35` | `59` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 320–325 | 6 | 1 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 668: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (RT) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '20' (C) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [144–160], lower_priority='Action_PullBlock' annotated_start=147, effective_Action_PullBlock_start=161.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (RG) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
- ⚠️ Action 'Action_PullLeadBlock' range [147-221] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [224-243] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-259] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-321] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-225] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-311] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-286] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 144, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [144-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-309] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [144-160] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [165-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [232-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-259] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [147-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-233] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-329] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-264] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-295] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-317] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-288] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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