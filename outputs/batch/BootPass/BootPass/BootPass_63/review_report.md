# Play-Annotation-Generator Annotation Review — BootPass_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_63`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 110 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 111 | START | 111 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `16` | `16` | 121 | START | 121 | 131 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `17` | `17` | 121 | START | 129 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `2` | `2` | 121 | START | 121 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `20` | `20` | 121 | START | 121 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `21` | `21` | 121 | START | 121 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 128 | END | 111 | 128 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `9` | `9` | 133 | START | 133 | 152 |
| ✅ EXACT | `Action_BootAway` | QB | `9` | `9` | 153 | START | 153 | 179 |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | `14` | `14` | 164 | START | 164 | 184 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 180 | START | 180 | 192 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `14` | `14` | 203 | START | 203 | 212 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_FakeHandoff` | 133 | 152 | 20 | inferred_complete_timeline |
| `Action_BootAway` | 153 | 179 | 27 | inferred_complete_timeline |
| `Action_ThrowPass` | 180 | 192 | 13 | inferred_complete_timeline |
| `Action_None` | 193 | 329 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 223 | 113 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 164 | 184 | 21 | inferred_complete_timeline |
| `Action_None` | 185 | 202 | 18 | inferred_complete_timeline |
| `Action_SecureCatch` | 203 | 212 | 10 | inferred_complete_timeline |
| `Action_None` | 213 | 277 | 65 | inferred_complete_timeline |
| `Action_None` | 279 | 287 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 318 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 298 | 188 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 328 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 304 | 194 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 297 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_RunBlock` | 121 | 181 | 61 | inferred_complete_timeline |
| `Action_RunBlock` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_RunBlock` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 329 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallSnap` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 129 | 133 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_RunBlock` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 329 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_RunBlock` | 121 | 189 | 69 | inferred_complete_timeline |
| `Action_RunBlock` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 197 | 329 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 179 | 69 | inferred_complete_timeline |
| `Action_None` | 183 | 201 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 146 | 36 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 291 | 181 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 329 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 142 | 32 | inferred_complete_timeline |
| `Action_None` | 144 | 234 | 91 | inferred_complete_timeline |
| `Action_None` | 241 | 245 | 5 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 142 | 32 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 278 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 179 | 69 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |
| `Action_None` | 301 | 308 | 8 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 231 | 121 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 316 | 9 | inferred_complete_timeline |
| `Action_None` | 320 | 326 | 7 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 133 | 23 | inferred_complete_timeline |
| `Action_None` | 135 | 191 | 57 | inferred_complete_timeline |
| `Action_None` | 198 | 329 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 126–329 | 204 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 176–183 | 8 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 178–190 | 13 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 191–209 | 11 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 192–329 | 137 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 225–329 | 92 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 234–272 | 39 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 244–329 | 86 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 291–329 | 39 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 303–329 | 10 | 4 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (3 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `17` (C): Annotated start 121 != Inferred start 129
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [111–128], lower_priority='Action_RunBlock' annotated_start=121, effective_Action_RunBlock_start=129.
- ⚠️ Action 'Action_None' range [111-304] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [121-189] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [193-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [197-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-326] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-201] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-298] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-277] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-287] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-318] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-291] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [121-131] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [133-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [146-329] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [129-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-133] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-329] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [121-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [121-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [131-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-329] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-242] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-329] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '34' has 1 frames without a visible bounding box.
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