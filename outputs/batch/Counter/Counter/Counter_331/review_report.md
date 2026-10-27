# Play-Annotation-Generator Annotation Review — Counter_331

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_331`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | TE | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | TE | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 135 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 133 | START | 133 | 146 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `15` | `14` | 136 | START | 147 | 222 |
| ✅ EXACT | `Action_DownBlock` | LG | `20` | `19` | 136 | START | 136 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `7` | `6` | 136 | START | 136 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 136 | START | 136 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `3` | `2` | 136 | START | 136 | 182 |
| ✅ EXACT | `Action_SnapReceive` | TE | `13` | `12` | 146 | END | 133 | 146 |
| ✅ EXACT | `Action_Handoff` | TE | `13` | `12` | 158 | START | 158 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 178 | START | 178 | 204 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 222 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 204 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 212 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 219 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 274 | 142 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 329 | 197 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 329 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_SnapReceive` | 133 | 146 | 14 | inferred_complete_timeline |
| `Action_None` | 147 | 157 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 177 | 20 | inferred_complete_timeline |
| `Action_None` | 178 | 188 | 11 | inferred_complete_timeline |
| `Action_None` | 193 | 209 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 203 | 68 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 222 | 17 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 222 | 87 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_BallSnap` | 133 | 146 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 222 | 76 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PullBlock` | 136 | 172 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 192 | 222 | 31 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 156 | 24 | inferred_complete_timeline |
| `Action_None` | 159 | 265 | 107 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 329 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 248 | 116 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 329 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 168 | 36 | inferred_complete_timeline |
| `Action_None` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_None` | 191 | 250 | 60 | inferred_complete_timeline |
| `Action_None` | 261 | 301 | 41 | inferred_complete_timeline |
| `Action_None` | 303 | 329 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 329 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 152 | 20 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 184 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 224 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 316 | 184 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 283 | 151 | inferred_complete_timeline |
| `Action_None` | 287 | 329 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 301 | 169 | inferred_complete_timeline |
| `Action_None` | 309 | 313 | 5 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 329 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_None` | 133 | 273 | 141 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–191 | 186 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–294 | 294 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–83 | 73 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 15–329 | 223 | 13 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 169–243 | 26 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 170–188 | 18 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 186–192 | 7 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 189–326 | 136 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 194–329 | 134 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 199–203 | 5 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 202–272 | 12 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 218–329 | 112 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 220–329 | 108 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 231–260 | 29 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 242–326 | 62 | 6 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 258–304 | 22 | 4 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 284–329 | 37 | 3 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 288–301 | 8 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 296–329 | 26 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `15` (C): Annotated start 136 != Inferred start 147
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 663: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 664: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [133–146], lower_priority='Action_DownBlock' annotated_start=136, effective_Action_DownBlock_start=147.
- ⚠️ Action 'Action_None' range [133-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [136-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [189-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-250] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-329] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-219] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-316] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-294] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-301] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-222] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-265] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [136-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [188-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-25] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-45] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-313] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-326] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-250] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-255] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-277] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-311] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-326] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-304] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-293] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>