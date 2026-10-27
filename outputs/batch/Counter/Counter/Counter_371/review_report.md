# Play-Annotation-Generator Annotation Review — Counter_371

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_371`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 136
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 32 | START | 32 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 35 | START | 35 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `22` | `21` | 35 | START | 35 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `16` | `15` | 35 | START | 47 | 71 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `2` | `1` | 35 | START | 35 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 46 | END | 32 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 73 | START | 73 | 100 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–308
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_None` | 47 | 72 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 100 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 141 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 187 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 224 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 306 | 308 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 359 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 139 | 108 | inferred_complete_timeline |
| `Action_None` | 141 | 174 | 34 | inferred_complete_timeline |
| `Action_None` | 187 | 199 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 233 | 334 | 102 | inferred_complete_timeline |
| `Action_None` | 347 | 357 | 11 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 359 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 333 | 302 | inferred_complete_timeline |
| `Action_None` | 336 | 359 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 197 | 166 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |
| `Action_None` | 211 | 356 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 35 | 53 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 125 | 21 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 42 | 54 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 47 | 71 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 73 | 127 | 55 | inferred_complete_timeline |
| `Action_None` | 128 | 318 | 191 | inferred_complete_timeline |
| `Action_None` | 340 | 352 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 114 | 83 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 152 | 26 | inferred_complete_timeline |
| `Action_None` | 157 | 178 | 22 | inferred_complete_timeline |
| `Action_None` | 181 | 232 | 52 | inferred_complete_timeline |
| `Action_None` | 235 | 242 | 8 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_None` | 275 | 305 | 31 | inferred_complete_timeline |
| `Action_None` | 308 | 315 | 8 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 333 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 35 | 81 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 73 | 42 | inferred_complete_timeline |
| `Action_None` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 119 | 88 | inferred_complete_timeline |
| `Action_None` | 130 | 197 | 68 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_None` | 222 | 245 | 24 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |
| `Action_None` | 256 | 359 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 173 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 109 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 154 | 123 | inferred_complete_timeline |
| `Action_None` | 158 | 359 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 142 | 111 | inferred_complete_timeline |
| `Action_None` | 159 | 288 | 130 | inferred_complete_timeline |
| `Action_None` | 292 | 359 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 142 | 111 | inferred_complete_timeline |
| `Action_None` | 153 | 262 | 110 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 291 | 3 | inferred_complete_timeline |
| `Action_None` | 294 | 303 | 10 | inferred_complete_timeline |
| `Action_None` | 306 | 311 | 6 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 331 | 4 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 339 | 344 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 359 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 321 | 290 | inferred_complete_timeline |
| `Action_None` | 326 | 328 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 258 | 227 | inferred_complete_timeline |
| `Action_None` | 260 | 296 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 288 | 257 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_None` | 315 | 359 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 68–170 | 103 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–359 | 217 | 14 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 76–93 | 13 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 85–359 | 228 | 11 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 115–358 | 225 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 169–174 | 6 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 193–359 | 167 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 237–359 | 103 | 8 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 324–359 | 36 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 344–359 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (13 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '15' (C) duration 93 frames exceeds threshold 90 frames [start=35, end=127].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [32–46], lower_priority='Action_PullBlock' annotated_start=35, effective_Action_PullBlock_start=47.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 93 frames exceeds threshold 90 frames [start=35, end=127].
- ⚠️ Action 'Action_None' range [32-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [35-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-333] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-288] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-288] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-334] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-357] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-356] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-141] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-224] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [298-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [306-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [47-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-318] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-352] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-262] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-152] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-232] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-305] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-315] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-258] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-296] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [35-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [42-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [35-53] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-170] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-189] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-314] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-326] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-337] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-124] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-185] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-211] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-173] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-358] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-326] for track '30' has 2 frames without a visible bounding box.
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