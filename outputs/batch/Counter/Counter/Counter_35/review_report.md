# Play-Annotation-Generator Annotation Review — Counter_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_35`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 8 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 8 | START | 8 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 8 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 8 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 8 | START | 8 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 8 | START | 8 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 8 | START | 8 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 8 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 8 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 8 | START | 8 | 156 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `6` | `5` | 99 | START | 99 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 103 | START | 103 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `6` | `5` | 103 | START | 103 | 121 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `17` | `16` | 103 | START | 103 | 195 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `10` | `9` | 103 | START | 103 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 114 | END | 99 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 123 | START | 123 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `9` | `8` | 157 | START | 157 | 290 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 195 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–303
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 123 | 156 | 34 | inferred_complete_timeline |
| `Action_None` | 157 | 303 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–241
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 138 | 40 | inferred_complete_timeline |
| `Action_None` | 140 | 179 | 40 | inferred_complete_timeline |
| `Action_None` | 183 | 226 | 44 | inferred_complete_timeline |
| `Action_None` | 231 | 241 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 249 | 151 | inferred_complete_timeline |
| `Action_None` | 259 | 359 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 8–350
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 156 | 149 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 290 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 306 | 310 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 349 | 350 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 8–319
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 102 | 95 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 195 | 93 | inferred_complete_timeline |
| `Action_None` | 196 | 313 | 118 | inferred_complete_timeline |
| `Action_None` | 316 | 319 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–263
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 102 | 95 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 103 | 195 | 93 | inferred_complete_timeline |
| `Action_None` | 196 | 260 | 65 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 8–295
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 120 | 22 | inferred_complete_timeline |
| `Action_None` | 128 | 283 | 156 | inferred_complete_timeline |
| `Action_None` | 285 | 295 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 136 | 38 | inferred_complete_timeline |
| `Action_None` | 140 | 359 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–359
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 102 | 95 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 122 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 195 | 58 | inferred_complete_timeline |
| `Action_None` | 196 | 304 | 109 | inferred_complete_timeline |
| `Action_None` | 317 | 359 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 8–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 30 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 40 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 98 | 57 | inferred_complete_timeline |
| `Action_None` | 99 | 264 | 166 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 311 | 40 | inferred_complete_timeline |
| `Action_None` | 314 | 321 | 8 | inferred_complete_timeline |
| `Action_None` | 329 | 330 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 347 | 16 | inferred_complete_timeline |
| `Action_None` | 349 | 359 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 8–121
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 121 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 296 | 198 | inferred_complete_timeline |
| `Action_None` | 303 | 306 | 4 | inferred_complete_timeline |
| `Action_None` | 319 | 359 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 134 | 36 | inferred_complete_timeline |
| `Action_None` | 136 | 246 | 111 | inferred_complete_timeline |
| `Action_None` | 248 | 263 | 16 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 280 | 11 | inferred_complete_timeline |
| `Action_None` | 283 | 307 | 25 | inferred_complete_timeline |
| `Action_None` | 312 | 315 | 4 | inferred_complete_timeline |
| `Action_None` | 333 | 336 | 4 | inferred_complete_timeline |
| `Action_None` | 341 | 359 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 8–139
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 139 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 8–348
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |
| `Action_None` | 242 | 348 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 214 | 116 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 240 | 359 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 227 | 129 | inferred_complete_timeline |
| `Action_None` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_None` | 276 | 333 | 58 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 229 | 131 | inferred_complete_timeline |
| `Action_None` | 232 | 253 | 22 | inferred_complete_timeline |
| `Action_None` | 257 | 328 | 72 | inferred_complete_timeline |
| `Action_None` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 322 | 224 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–339
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 322 | 224 | inferred_complete_timeline |
| `Action_None` | 333 | 339 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–319
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 238 | 140 | inferred_complete_timeline |
| `Action_None` | 241 | 319 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 8–359 | 349 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 51–169 | 9 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 99–106 | 8 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 117–348 | 223 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 131–359 | 188 | 11 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 177–195 | 19 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 270–295 | 15 | 3 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 272–299 | 8 | 3 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 274–336 | 56 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 275–359 | 76 | 5 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 281–302 | 9 | 3 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 327–359 | 33 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 334–336 | 3 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 339–359 | 17 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 102 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 72: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (Unknown) duration 93 frames exceeds threshold 90 frames [start=103, end=195].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (TE1) duration 93 frames exceeds threshold 90 frames [start=103, end=195].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 93 frames exceeds threshold 90 frames [start=103, end=195].
- ⚠️ Action 'Action_None' range [99-249] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-227] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-333] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-322] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-339] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-322] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-246] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-263] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-280] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-307] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-290] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [306-310] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [349-350] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-229] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-319] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-296] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-359] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-359] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-313] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-121] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-348] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-139] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-304] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-30] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-40] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-347] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-269] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-335] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-169] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-322] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-287] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-313] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-330] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-359] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-348] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>