# Play-Annotation-Generator Annotation Review — JetSweep_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_88`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 7 | START | 4 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 7 | START | 4 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 7 | START | 4 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 7 | START | 4 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 7 | START | 4 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 7 | START | 4 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 7 | START | 4 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 7 | START | 4 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 7 | START | 4 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 7 | START | 4 | 127 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `7` | `6` | 128 | START | 128 | 182 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 152 | START | 152 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RT | `10` | `9` | 153 | START | 153 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 153 | START | 164 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 153 | START | 164 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `14` | 153 | START | 153 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `16` | 153 | START | 153 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `17` | 153 | START | 153 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 163 | END | 152 | 163 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 171 | START | 171 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `7` | `6` | 183 | START | 183 | 294 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `19` | `18` | 187 | START | 187 | 244 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 271 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_SnapReceive` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_None` | 164 | 170 | 7 | inferred_complete_timeline |
| `Action_Toss` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_None` | 192 | 389 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–326
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 326 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 389 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–375
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 127 | 124 | inferred_complete_timeline |
| `Action_JetMotion` | 128 | 182 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 294 | 112 | inferred_complete_timeline |
| `Action_BallCarry` | 296 | 375 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |
| `Action_None` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_None` | 313 | 338 | 26 | inferred_complete_timeline |
| `Action_None` | 346 | 371 | 26 | inferred_complete_timeline |
| `Action_None` | 374 | 387 | 14 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–374
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 152 | 149 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 199 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 233 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 271 | 36 | inferred_complete_timeline |
| `Action_None` | 272 | 374 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 4–387
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 152 | 149 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 205 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 240 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 243 | 271 | 29 | inferred_complete_timeline |
| `Action_None` | 272 | 284 | 13 | inferred_complete_timeline |
| `Action_None` | 286 | 300 | 15 | inferred_complete_timeline |
| `Action_None` | 303 | 387 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–307
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_BallSnap` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 164 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 271 | 91 | inferred_complete_timeline |
| `Action_None` | 272 | 287 | 16 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–387
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 44 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 152 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 175 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 233 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 271 | 35 | inferred_complete_timeline |
| `Action_None` | 272 | 277 | 6 | inferred_complete_timeline |
| `Action_None` | 281 | 290 | 10 | inferred_complete_timeline |
| `Action_None` | 299 | 307 | 9 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_None` | 319 | 387 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 152 | 149 | inferred_complete_timeline |
| `Action_LeadBlock` | 153 | 241 | 89 | inferred_complete_timeline |
| `Action_LeadBlock` | 245 | 258 | 14 | inferred_complete_timeline |
| `Action_LeadBlock` | 260 | 271 | 12 | inferred_complete_timeline |
| `Action_None` | 272 | 281 | 10 | inferred_complete_timeline |
| `Action_None` | 306 | 389 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–241
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 241 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 186 | 183 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 187 | 244 | 58 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 251 | 271 | 21 | inferred_complete_timeline |
| `Action_None` | 272 | 389 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 8–389
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 151 | 140 | inferred_complete_timeline |
| `Action_None` | 152 | 379 | 228 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–338
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 236 | 85 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |
| `Action_None` | 331 | 338 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 151 | 138 | inferred_complete_timeline |
| `Action_None` | 152 | 230 | 79 | inferred_complete_timeline |
| `Action_None` | 234 | 389 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 389 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 211 | 60 | inferred_complete_timeline |
| `Action_None` | 219 | 227 | 9 | inferred_complete_timeline |
| `Action_None` | 236 | 352 | 117 | inferred_complete_timeline |
| `Action_None` | 354 | 368 | 15 | inferred_complete_timeline |
| `Action_None` | 371 | 389 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–267
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 267 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 389 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–218
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 151 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 218 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 4–383 | 367 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 4–46 | 27 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 17–389 | 360 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 228–389 | 151 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 248–389 | 137 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 296–303 | 4 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 297–388 | 78 | 6 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 297–301 | 4 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 335–389 | 55 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 337–389 | 46 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 352–377 | 10 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 372–383 | 11 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 178: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Overlapping action conflict at frame 153 for track '9': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '9' (RT) duration 119 frames exceeds threshold 90 frames [start=153, end=271].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 119 frames exceeds threshold 90 frames [start=153, end=271].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [152–163], lower_priority='Action_ZoneBlock' annotated_start=153, effective_Action_ZoneBlock_start=164.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 119 frames exceeds threshold 90 frames [start=153, end=271].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LT) duration 119 frames exceeds threshold 90 frames [start=153, end=271].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 119 frames exceeds threshold 90 frames [start=153, end=271].
- ⚠️ Action 'Action_None' range [152-326] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-338] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-371] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-387] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [296-375] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-352] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-368] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-351] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-383] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [153-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [245-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-389] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '10' starts at frame 164, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [164-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-338] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [210-216] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-284] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-300] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-387] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-271] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-374] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-233] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-271] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-387] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [187-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-9] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-151] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-379] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-52] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-300] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-328] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-352] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-283] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-316] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-369] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-377] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>