# Play-Annotation-Generator Annotation Review — Counter_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_59`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 151
- **Validation Warnings:** 180
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 176 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 177 | START | 177 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `10` | 180 | START | 180 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 180 | START | 195 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `3` | 180 | START | 180 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 180 | START | 180 | 233 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `1` | `0` | 180 | START | 180 | 225 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 194 | END | 177 | 194 |
| ✅ EXACT | `Action_BallCarry` | QB | `2` | `1` | 219 | START | 219 | 245 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 274 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_SnapReceive` | 177 | 194 | 18 | inferred_complete_timeline |
| `Action_None` | 195 | 218 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 245 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 241 | 65 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 255 | 79 | inferred_complete_timeline |
| `Action_None` | 257 | 317 | 61 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 293 | 117 | inferred_complete_timeline |
| `Action_None` | 295 | 419 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 180 | 225 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 179 | 98 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 196 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 234 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 250 | 15 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 319 | 382 | 64 | inferred_complete_timeline |
| `Action_None` | 385 | 390 | 6 | inferred_complete_timeline |
| `Action_None` | 393 | 419 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 189 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 274 | 78 | inferred_complete_timeline |
| `Action_None` | 357 | 410 | 54 | inferred_complete_timeline |
| `Action_None` | 417 | 419 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_BallSnap` | 177 | 194 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 195 | 234 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 250 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 179 | 95 | inferred_complete_timeline |
| `Action_PullBlock` | 180 | 233 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 237 | 241 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 224 | 48 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 234 | 58 | inferred_complete_timeline |
| `Action_None` | 237 | 247 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 228 | 52 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 286 | 374 | 89 | inferred_complete_timeline |
| `Action_None` | 379 | 393 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 176 | 92 | inferred_complete_timeline |
| `Action_None` | 177 | 229 | 53 | inferred_complete_timeline |
| `Action_None` | 236 | 247 | 12 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 263 | 12 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 308 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 200 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 225 | 49 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 299 | 123 | inferred_complete_timeline |
| `Action_None` | 318 | 323 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 313 | 137 | inferred_complete_timeline |
| `Action_None` | 327 | 419 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 360 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 350 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 233 | 57 | inferred_complete_timeline |
| `Action_None` | 235 | 288 | 54 | inferred_complete_timeline |
| `Action_None` | 291 | 313 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–419 | 399 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 98–419 | 311 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 230–235 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 249–305 | 24 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 266–273 | 8 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 277–295 | 14 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 278–419 | 117 | 5 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 282–332 | 34 | 5 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 289–419 | 125 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 289–317 | 26 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 291–419 | 102 | 6 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 296–300 | 5 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 300–419 | 78 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 303–357 | 54 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 313–419 | 107 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 332–419 | 88 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 345–419 | 72 | 3 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 345–419 | 72 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 347–387 | 38 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 353–357 | 5 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 358–419 | 46 | 5 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 358–367 | 9 | 2 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 370–418 | 46 | 2 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 390–419 | 25 | 3 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 393–394 | 2 | 1 | Undefined position; Undefined team |
| `46` | `54` | Position_Unknown | Team_Unknown | 395–419 | 25 | 1 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 403–405 | 3 | 1 | Undefined position; Undefined team |
| `48` | `56` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `49` | `57` | Position_Unknown | Team_Unknown | 418–419 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 120: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=180, end=274].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (LG) duration 95 frames exceeds threshold 90 frames [start=180, end=274].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [177–194], lower_priority='Action_DownBlock' annotated_start=180, effective_Action_DownBlock_start=195.
- ⚠️ Action 'Action_PullLeadBlock' range [180-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [180-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [205-234] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-382] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-390] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-374] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-393] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-317] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-350] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [180-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-274] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-410] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-313] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-419] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-360] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [195-234] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [237-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [244-250] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-288] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-313] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-293] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-419] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [180-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [237-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-229] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-247] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-398] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-419] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-318] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-363] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-357] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-374] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-396] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-411] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-325] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-408] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-311] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-357] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-419] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-357] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-382] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-357] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-385] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-411] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-418] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-396] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-405] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.

</details>