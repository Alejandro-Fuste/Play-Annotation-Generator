# Play-Annotation-Generator Annotation Review — Dagger_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_12`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 131
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BreakInside` | WR2 | offense | `17` | `17` |
| ✅ EXACT | `Action_ClearToEdge` | DE2 | defense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 133 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 134 | START | 134 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `14` | 137 | START | 137 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 137 | START | 137 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 137 | START | 137 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 137 | START | 137 | 150 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `8` | `8` | 137 | START | 140 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 139 | END | 134 | 139 |
| ✅ EXACT | `Action_BreakInside` | WR2 | `17` | `17` | 155 | START | 155 | 275 |
| ✅ EXACT | `Action_ClearToEdge` | DE2 | `5` | `5` | 155 | START | 155 | 236 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `18` | `18` | 227 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_SnapReceive` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_None` | 140 | 153 | 14 | inferred_complete_timeline |
| `Action_None` | 155 | 224 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 181 | 48 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_BreakInside` | 155 | 275 | 121 | inferred_complete_timeline |
| `Action_None` | 277 | 290 | 14 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 307 | 7 | inferred_complete_timeline |
| `Action_None` | 309 | 329 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 158 | 25 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 329 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |
| `Action_None` | 157 | 206 | 50 | inferred_complete_timeline |
| `Action_None` | 217 | 222 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 219 | 224 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_BallSnap` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 147 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 149 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 196 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 149 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_ClearToEdge` | 155 | 236 | 82 | inferred_complete_timeline |
| `Action_None` | 237 | 244 | 8 | inferred_complete_timeline |
| `Action_None` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_None` | 255 | 274 | 20 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 292 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 226 | 11 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 150 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 181 | 48 | inferred_complete_timeline |
| `Action_None` | 183 | 298 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 329 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 163 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 327 | 194 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 205 | 72 | inferred_complete_timeline |
| `Action_None` | 222 | 233 | 12 | inferred_complete_timeline |
| `Action_None` | 236 | 243 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 253 | 120 | inferred_complete_timeline |
| `Action_None` | 256 | 329 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 213 | 80 | inferred_complete_timeline |
| `Action_None` | 215 | 329 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–158 | 153 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 175–205 | 15 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 200–317 | 118 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 203–254 | 14 | 5 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 220–224 | 4 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 243–317 | 75 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 252–257 | 6 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 278–286 | 9 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 285–329 | 44 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 299–301 | 3 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 323–327 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `8` (C): Annotated start 137 != Inferred start 140
- ❌ Missing segment for action `Action_ThrowPass` on target `18` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 18: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [134–139], lower_priority='Action_PassBlock' annotated_start=137, effective_Action_PassBlock_start=140.
- ⚠️ Segment 'Action_ThrowPass' for track '18' has invalid range: start=227, end=224. Clamping end to start.
- ⚠️ Action 'Action_None' range [134-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-158] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-274] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-181] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-298] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-327] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-187] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [201-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-253] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [155-275] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-290] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-224] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [181-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-205] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [216-217] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [219-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [216-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [219-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [223-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-317] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-317] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-293] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>