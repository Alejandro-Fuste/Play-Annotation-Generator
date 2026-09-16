# Play-Annotation-Generator Annotation Review — BootPass_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_1`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 184
- **Validation Warnings:** 208
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 159
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_RunBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_SecureCatch` | RB | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 5 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 183 |
| ✅ EXACT | `Action_RunBlock` | LT | `13` | `13` | 77 | START | 77 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `15` | `15` | 77 | START | 77 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `17` | `17` | 77 | START | 77 | 83 |
| ⚠️ START CHANGED | `Action_RunBlock` | RG | `20` | `20` | 77 | START | 78 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `4` | 86 | END | 86 | 86 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `4` | `4` | 98 | START | 98 | 110 |
| ✅ EXACT | `Action_BootAway` | QB | `4` | `4` | 111 | START | 111 | 150 |
| ✅ EXACT | `Action_RunFlatRoute` | WR1 | `1` | `1` | 116 | START | 116 | 167 |
| ✅ EXACT | `Action_ThrowPass` | QB | `4` | `4` | 162 | START | 162 | 175 |
| ✅ EXACT | `Action_SecureCatch` | RB | `3` | `3` | 226 | START | 226 | 235 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 86 | 1 | inferred_complete_timeline |
| `Action_None` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_FakeHandoff` | 98 | 110 | 13 | inferred_complete_timeline |
| `Action_BootAway` | 111 | 150 | 40 | inferred_complete_timeline |
| `Action_None` | 151 | 161 | 11 | inferred_complete_timeline |
| `Action_ThrowPass` | 162 | 175 | 14 | inferred_complete_timeline |
| `Action_None` | 176 | 191 | 16 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_SecureCatch` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_None` | 236 | 249 | 14 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |
| `Action_None` | 280 | 285 | 6 | inferred_complete_timeline |
| `Action_None` | 295 | 311 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 116 | 167 | 52 | inferred_complete_timeline |
| `Action_None` | 168 | 286 | 119 | inferred_complete_timeline |
| `Action_None` | 290 | 316 | 27 | inferred_complete_timeline |
| `Action_None` | 325 | 332 | 8 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 359 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 187 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 86 | 170 | 85 | inferred_complete_timeline |
| `Action_RunBlock` | 173 | 191 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 238 | 257 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 260 | 359 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–86
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 11 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 58 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 73 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 78 | 86 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_RunBlock` | 119 | 164 | 46 | inferred_complete_timeline |
| `Action_RunBlock` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 176 | 191 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 239 | 240 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 101 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 251 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 298 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 333 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 35–160
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 82 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 122 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 160 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 191 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 197 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 359 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 282 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 311 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 336 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–184 | 181 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–99 | 100 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 98–359 | 256 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 114–359 | 183 | 9 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 129–332 | 132 | 11 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 154–359 | 189 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 174–359 | 186 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 185–227 | 43 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 202–359 | 88 | 9 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 210–233 | 20 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 214–359 | 145 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 235–359 | 102 | 10 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 238–359 | 109 | 5 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 243–359 | 102 | 5 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 245–359 | 80 | 5 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 246–265 | 17 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 261–359 | 71 | 7 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 267–359 | 72 | 3 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 300–347 | 21 | 5 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 348–352 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (12 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (6 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `20` (RG): Annotated start 77 != Inferred start 78

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF3` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 163 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-359] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-286] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-316] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-311] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-197] for track '6' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-359] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-183] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-191] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-282] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-336] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-187] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-251] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-298] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-333] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [88-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [94-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [119-164] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [171-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [176-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [194-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [213-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [222-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [231-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [235-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [239-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-179] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [86-170] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [173-191] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [196-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [238-257] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [260-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [78-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-122] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-162] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-198] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-266] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-178] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-270] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-291] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-312] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-332] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-199] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-282] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-227] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-207] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-218] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-244] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-296] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-315] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-227] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-246] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-252] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-257] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-281] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-307] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-319] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-257] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-336] for track '32' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-359] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-274] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-282] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-284] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-324] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-348] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-260] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-317] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-330] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-359] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-278] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-319] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-359] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-310] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-347] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-352] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>