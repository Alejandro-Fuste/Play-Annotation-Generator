# Play-Annotation-Generator Annotation Review — SplitZone_208

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_208`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 174
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 26 | START | 27 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 26 | START | 27 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 26 | START | 27 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 26 | START | 27 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 26 | START | 27 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 26 | START | 27 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 26 | START | 27 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 26 | START | 27 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 26 | START | 27 | 198 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `16` | `16` | 190 | START | 191 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 193 | START | 193 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 193 | START | 202 | 223 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 193 | START | 193 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 193 | START | 193 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 193 | START | 193 | 204 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `7` | `7` | 199 | START | 199 | 207 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 201 | END | 190 | 201 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 207 | START | 207 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 215 | START | 215 | 223 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 287 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 27–265
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 189 | 163 | inferred_complete_timeline |
| `Action_SnapReceive` | 190 | 201 | 12 | inferred_complete_timeline |
| `Action_None` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 214 | 8 | inferred_complete_timeline |
| `Action_None` | 215 | 265 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 27–337
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 214 | 188 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 232 | 316 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 337 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 27–448
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 189 | 163 | inferred_complete_timeline |
| `Action_None` | 190 | 233 | 44 | inferred_complete_timeline |
| `Action_None` | 237 | 301 | 65 | inferred_complete_timeline |
| `Action_None` | 303 | 448 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 27–233
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 198 | 172 | inferred_complete_timeline |
| `Action_SplitBlock` | 199 | 207 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_SplitBlock` | 228 | 233 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 27–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 192 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 27–229
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 36 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 192 | 150 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 219 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 34 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 223 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 238 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 287 | 47 | inferred_complete_timeline |
| `Action_None` | 288 | 311 | 24 | inferred_complete_timeline |
| `Action_None` | 333 | 364 | 32 | inferred_complete_timeline |
| `Action_None` | 374 | 449 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 27–403
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 192 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 211 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 245 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 268 | 275 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 288 | 320 | 33 | inferred_complete_timeline |
| `Action_None` | 324 | 403 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 192 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 204 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 287 | 81 | inferred_complete_timeline |
| `Action_None` | 288 | 343 | 56 | inferred_complete_timeline |
| `Action_None` | 350 | 376 | 27 | inferred_complete_timeline |
| `Action_None` | 378 | 381 | 4 | inferred_complete_timeline |
| `Action_None` | 385 | 449 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 55–266
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 55 | 187 | 133 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 60–243
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 123 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 189 | 63 | inferred_complete_timeline |
| `Action_None` | 190 | 203 | 14 | inferred_complete_timeline |
| `Action_None` | 233 | 243 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 84–291
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 84 | 147 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 189 | 39 | inferred_complete_timeline |
| `Action_None` | 190 | 226 | 37 | inferred_complete_timeline |
| `Action_None` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 267 | 12 | inferred_complete_timeline |
| `Action_None` | 270 | 291 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 80–449
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 80 | 166 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 189 | 21 | inferred_complete_timeline |
| `Action_None` | 190 | 221 | 32 | inferred_complete_timeline |
| `Action_None` | 224 | 241 | 18 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_None` | 268 | 298 | 31 | inferred_complete_timeline |
| `Action_None` | 312 | 325 | 14 | inferred_complete_timeline |
| `Action_None` | 328 | 449 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 27–243
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 47 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 189 | 133 | inferred_complete_timeline |
| `Action_None` | 190 | 243 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 27–265
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 80 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 115 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 189 | 63 | inferred_complete_timeline |
| `Action_None` | 190 | 226 | 37 | inferred_complete_timeline |
| `Action_None` | 261 | 265 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 31–449
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 189 | 159 | inferred_complete_timeline |
| `Action_None` | 190 | 246 | 57 | inferred_complete_timeline |
| `Action_None` | 249 | 370 | 122 | inferred_complete_timeline |
| `Action_None` | 387 | 449 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `26`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 133–177
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 133 | 138 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 177 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 27–35 | 9 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 27–126 | 90 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 27–51 | 25 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 27–281 | 113 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 27–55 | 28 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 27–62 | 36 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 37–42 | 6 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 48–52 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 207–291 | 83 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 210–249 | 39 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 211–429 | 215 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 234–449 | 177 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 242–246 | 5 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 253–449 | 179 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 258–350 | 93 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 286–416 | 122 | 3 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 288–449 | 155 | 3 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 300–443 | 138 | 3 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 315–449 | 115 | 5 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 341–449 | 102 | 3 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 370–449 | 76 | 2 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 376–378 | 3 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 388–391 | 4 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 421–449 | 29 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 434–449 | 7 | 3 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 436–449 | 14 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 447–448 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (C): Annotated start 190 != Inferred start 191
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `24` (actor_track_id `26`): `SAF1` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 95 frames exceeds threshold 90 frames [start=193, end=287].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 95 frames exceeds threshold 90 frames [start=193, end=287].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 95 frames exceeds threshold 90 frames [start=193, end=287].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [190–201], lower_priority='Action_ZoneBlock' annotated_start=193, effective_Action_ZoneBlock_start=202.
- ⚠️ Action 'Action_PreSnap' range [27-189] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-448] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-255] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [268-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-403] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-337] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-35] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-287] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-343] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-376] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [199-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [209-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [228-233] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-40] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-51] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-36] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [228-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-53] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-223] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-311] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-364] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-370] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-52] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-221] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-241] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-325] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-226] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-249] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-309] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-429] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-342] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-400] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-350] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-398] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-363] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-374] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-311] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-443] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-353] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-367] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-405] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-426] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-350] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-427] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-403] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-391] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>