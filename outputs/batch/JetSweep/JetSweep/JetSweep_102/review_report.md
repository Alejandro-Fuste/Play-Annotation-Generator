# Play-Annotation-Generator Annotation Review — JetSweep_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_102`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `9` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | OLB2 | defense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `9` | `8` | 140 | START | 140 | 194 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 167 | START | 167 | 177 |
| ✅ EXACT | `Action_LeadBlock` | TE | `12` | `11` | 171 | START | 171 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 171 | START | 171 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 171 | START | 178 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 171 | START | 171 | 187 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 171 | START | 171 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `5` | 171 | START | 171 | 191 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 177 | END | 167 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | OLB2 | `16` | `15` | 184 | START | 184 | 194 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 186 | START | 186 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `9` | `8` | 195 | START | 195 | 271 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 260 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_SnapReceive` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 185 | 8 | inferred_complete_timeline |
| `Action_Toss` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_None` | 195 | 291 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 335 | 169 | inferred_complete_timeline |
| `Action_None` | 342 | 389 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 201 | 35 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_JetMotion` | 140 | 194 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 271 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 335 | 343 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_LeadBlock` | 171 | 260 | 90 | inferred_complete_timeline |
| `Action_None` | 261 | 389 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 191 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 225 | 240 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 260 | 19 | inferred_complete_timeline |
| `Action_None` | 261 | 335 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 206 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_BallSnap` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 187 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 194 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 244 | 248 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 260 | 11 | inferred_complete_timeline |
| `Action_None` | 261 | 342 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 194 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 191 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 207 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 260 | 19 | inferred_complete_timeline |
| `Action_None` | 261 | 329 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 191 | 25 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 194 | 28 | inferred_complete_timeline |
| `Action_None` | 199 | 220 | 22 | inferred_complete_timeline |
| `Action_None` | 236 | 338 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 188 | 22 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 281 | 307 | 27 | inferred_complete_timeline |
| `Action_None` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_None` | 350 | 352 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–330
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 310 | 144 | inferred_complete_timeline |
| `Action_None` | 313 | 330 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 227 | 61 | inferred_complete_timeline |
| `Action_None` | 243 | 249 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 342 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 183 | 184 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 184 | 194 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 203 | 218 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 220 | 224 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 277 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 309 | 143 | inferred_complete_timeline |
| `Action_None` | 338 | 389 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 335 | 169 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_None` | 167 | 283 | 117 | inferred_complete_timeline |
| `Action_None` | 287 | 298 | 12 | inferred_complete_timeline |
| `Action_None` | 307 | 321 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 100–119 | 11 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 117–124 | 7 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 243–389 | 147 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 245–389 | 145 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 245–335 | 91 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 245–364 | 120 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 245–327 | 83 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 245–335 | 90 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 247–389 | 133 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 278–281 | 4 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 318–344 | 27 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 318–348 | 19 | 3 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 332–335 | 4 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 336–389 | 51 | 3 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 336–339 | 4 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 336–389 | 53 | 2 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 336–389 | 54 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 336–389 | 52 | 2 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 349–371 | 9 | 3 | Undefined position; Undefined team |
| `42` | `47` | Position_Unknown | Team_Unknown | 361–389 | 29 | 1 | Undefined position; Undefined team |
| `43` | `48` | Position_Unknown | Team_Unknown | 368–389 | 22 | 1 | Undefined position; Undefined team |
| `44` | `49` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |
| `45` | `50` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |
| `46` | `51` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (8 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [167–177], lower_priority='Action_ZoneBlock' annotated_start=171, effective_Action_ZoneBlock_start=178.
- ⚠️ Action 'Action_None' range [167-335] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-342] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-194] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-206] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [208-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [214-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [225-240] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-310] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-330] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-227] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-271] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-343] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-321] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-207] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [184-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [199-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [203-218] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [220-224] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-194] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-220] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-338] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-307] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-194] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [244-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-342] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-389] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-335] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-364] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-327] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-335] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-302] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-370] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-344] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-335] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-343] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-361] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-389] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-375] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>