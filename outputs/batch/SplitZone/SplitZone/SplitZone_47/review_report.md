# Play-Annotation-Generator Annotation Review — SplitZone_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_47`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
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
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | WR2 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 5 | START | 6 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 5 | START | 6 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 5 | START | 6 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 5 | START | 6 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 5 | START | 6 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 5 | START | 6 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 5 | START | 6 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 5 | START | 6 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 5 | START | 6 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 5 | START | 6 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 5 | START | 6 | 203 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 187 | START | 187 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 190 | START | 190 | 256 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `11` | 190 | START | 190 | 335 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 190 | START | 201 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 190 | START | 190 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 190 | START | 190 | 285 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 200 | END | 187 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `8` | `8` | 204 | START | 204 | 249 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 219 | START | 219 | 224 |
| ✅ EXACT | `Action_BlockSecondLevel` | WR2 | `1` | `1` | 222 | START | 222 | 335 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `0` | `0` | 225 | START | 225 | 334 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 335 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_SnapReceive` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_None` | 201 | 218 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_None` | 225 | 419 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 224 | 219 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 334 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 336 | 395 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 397 | 407 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 417 | 419 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 419 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 221 | 216 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 222 | 335 | 114 | inferred_complete_timeline |
| `Action_None` | 336 | 419 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 357 | 171 | inferred_complete_timeline |
| `Action_None` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_None` | 364 | 419 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 203 | 198 | inferred_complete_timeline |
| `Action_SplitBlock` | 204 | 249 | 46 | inferred_complete_timeline |
| `Action_SplitBlock` | 255 | 335 | 81 | inferred_complete_timeline |
| `Action_None` | 336 | 350 | 15 | inferred_complete_timeline |
| `Action_None` | 352 | 409 | 58 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 189 | 184 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 335 | 146 | inferred_complete_timeline |
| `Action_None` | 336 | 419 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 189 | 184 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 285 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 295 | 335 | 41 | inferred_complete_timeline |
| `Action_None` | 336 | 347 | 12 | inferred_complete_timeline |
| `Action_None` | 349 | 357 | 9 | inferred_complete_timeline |
| `Action_None` | 360 | 419 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_BallSnap` | 187 | 200 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 213 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 220 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 253 | 263 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 330 | 333 | 4 | inferred_complete_timeline |
| `Action_None` | 339 | 344 | 6 | inferred_complete_timeline |
| `Action_None` | 364 | 419 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 189 | 184 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 207 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 243 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 335 | 90 | inferred_complete_timeline |
| `Action_None` | 336 | 419 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 6–412
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 189 | 184 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 256 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 271 | 326 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 330 | 335 | 6 | inferred_complete_timeline |
| `Action_None` | 336 | 401 | 66 | inferred_complete_timeline |
| `Action_None` | 410 | 412 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–276
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 273 | 87 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–258
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 250 | 64 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 419 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 419 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 419 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 304 | 118 | inferred_complete_timeline |
| `Action_None` | 306 | 319 | 14 | inferred_complete_timeline |
| `Action_None` | 321 | 419 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 6–307
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 307 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 419 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 419 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 336 | 150 | inferred_complete_timeline |
| `Action_None` | 338 | 419 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 186 | 181 | inferred_complete_timeline |
| `Action_None` | 187 | 254 | 68 | inferred_complete_timeline |
| `Action_None` | 257 | 419 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 12–16 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 20–32 | 6 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 209–224 | 7 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 217–227 | 5 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 254–256 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 257–285 | 23 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 267–274 | 8 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 304–419 | 114 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 309–320 | 12 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 318–419 | 102 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 320–417 | 97 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 345–411 | 6 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 360–419 | 36 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '1' (WR2) duration 114 frames exceeds threshold 90 frames [start=222, end=335].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 146 frames exceeds threshold 90 frames [start=190, end=335].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 146 frames exceeds threshold 90 frames [start=190, end=335].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 146 frames exceeds threshold 90 frames [start=190, end=335].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [187–200], lower_priority='Action_ZoneBlock' annotated_start=190, effective_Action_ZoneBlock_start=201.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 146 frames exceeds threshold 90 frames [start=190, end=335].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 146 frames exceeds threshold 90 frames [start=190, end=335].
- ⚠️ Action 'Action_BallCarry' range [225-334] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [336-395] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [397-407] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [417-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-357] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [204-249] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [255-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-350] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-409] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [258-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [262-268] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [271-326] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-401] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-304] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-319] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-419] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-307] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-213] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-220] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [242-243] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [253-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [330-333] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-285] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-347] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-336] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-32] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-416] for track '30' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-414] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '35' has 1 frames without a visible bounding box.
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