# Play-Annotation-Generator Annotation Review — BootPass_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_55`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `36` | `26` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_RunFlatRoute` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 147 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `36` | `26` | 126 | START | 223 | 223 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 139 | START | 139 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 148 | START | 159 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `16` | `16` | 148 | START | 148 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `20` | `20` | 148 | START | 148 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 148 | START | 148 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `9` | `9` | 148 | START | 148 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 158 | END | 139 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `7` | `7` | 166 | START | 166 | 176 |
| ✅ EXACT | `Action_BootAway` | QB | `7` | `7` | 183 | START | 183 | 212 |
| ✅ EXACT | `Action_RunFlatRoute` | TE | `3` | `3` | 187 | START | 187 | 221 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 214 | START | 214 | 224 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_SnapReceive` | 139 | 158 | 20 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_FakeHandoff` | 166 | 176 | 11 | inferred_complete_timeline |
| `Action_FakeHandoff` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_BootAway` | 183 | 212 | 30 | inferred_complete_timeline |
| `Action_None` | 213 | 213 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 214 | 224 | 11 | inferred_complete_timeline |
| `Action_None` | 225 | 329 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 199 | 61 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 187 | 221 | 35 | inferred_complete_timeline |
| `Action_None` | 222 | 316 | 95 | inferred_complete_timeline |
| `Action_None` | 320 | 323 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 205 | 58 | inferred_complete_timeline |
| `Action_RunBlock` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 236 | 329 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 171 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 176 | 329 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_BallSnap` | 139 | 158 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 148 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 156 | 192 | 37 | inferred_complete_timeline |
| `Action_RunBlock` | 195 | 329 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 195 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 211 | 247 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 169 | 31 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 171 | 33 | inferred_complete_timeline |
| `Action_None` | 173 | 183 | 11 | inferred_complete_timeline |
| `Action_None` | 186 | 195 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 326 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 263 | 125 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 322 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 231 | 93 | inferred_complete_timeline |
| `Action_None` | 234 | 329 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 329 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 169–188 | 15 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 192–195 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 194–329 | 126 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 202–235 | 34 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 223–329 | 105 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 223–329 | 107 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 225–291 | 41 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_SecureCatch` for actor_track_id `36` (Position_Unknown): Annotated start 126 != Inferred start 223
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [139–158], lower_priority='Action_RunBlock' annotated_start=148, effective_Action_RunBlock_start=159.
- ⚠️ Segment 'Action_SecureCatch' for track '26' has invalid range: start=223, end=134. Clamping end to start.
- ⚠️ Action 'Action_None' range [139-322] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [166-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [148-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [202-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [211-247] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-326] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [139-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [159-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [166-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [148-171] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-171] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [148-205] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [207-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' for track '21' starts at frame 148, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunBlock' range [148-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [156-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-266] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-291] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '31' has 1 frames without a visible bounding box.
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

</details>