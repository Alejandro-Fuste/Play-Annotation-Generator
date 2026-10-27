# Play-Annotation-Generator Annotation Review — Counter_329

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_329`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 149
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 3
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | offense | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LG | offense | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 2 | START | 2 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `11` | `Group` | 2 | START | 2 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 2 | START | 2 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 2 | START | 2 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 2 | START | 2 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 2 | START | 2 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 2 | START | 2 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 2 | START | 2 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 2 | START | 2 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 2 | START | 2 | 204 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `20` | `19` | 158 | START | 162 | 163 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `20` | `19` | 161 | START | 179 | 183 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `20` | `19` | 161 | START | 179 | 183 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | `22` | `21` | 161 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LG | `17` | `16` | 161 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | QB | `4` | `3` | 161 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 171 | END | 158 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `4` | `3` | 188 | START | 188 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | TE | `9` | `8` | 205 | START | 205 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 259 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 2–323
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_SnapReceive` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 172 | 187 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 188 | 197 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 323 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 408 | 251 | inferred_complete_timeline |
| `Action_None` | 410 | 419 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–419
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 206 | 49 | inferred_complete_timeline |
| `Action_None` | 272 | 360 | 89 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 379 | 419 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–312
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 193 | 36 | inferred_complete_timeline |
| `Action_None` | 195 | 237 | 43 | inferred_complete_timeline |
| `Action_None` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_None` | 295 | 312 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–226
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 204 | 203 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 226 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 2–88
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 88 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–88
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 80 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 2–183
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 23 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 74 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 126 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 179 | 183 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–68
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 31 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 68 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–203
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 81 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 157 | 37 | inferred_complete_timeline |
| `Action_None` | 158 | 164 | 7 | inferred_complete_timeline |
| `Action_None` | 178 | 191 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 2–92
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 31 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 2–88
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 80 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 2–92
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 15 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 80 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 92 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–217
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 217 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–200
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 200 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 309 | 152 | inferred_complete_timeline |
| `Action_None` | 320 | 397 | 78 | inferred_complete_timeline |
| `Action_None` | 400 | 405 | 6 | inferred_complete_timeline |
| `Action_None` | 407 | 410 | 4 | inferred_complete_timeline |
| `Action_None` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 191 | 34 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 419 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 419 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 157 | 156 | inferred_complete_timeline |
| `Action_None` | 158 | 344 | 187 | inferred_complete_timeline |
| `Action_None` | 351 | 386 | 36 | inferred_complete_timeline |
| `Action_None` | 388 | 419 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 2–76 | 50 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 187–192 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 222–260 | 33 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 250–419 | 131 | 7 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 250–419 | 147 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 255–258 | 4 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 261–314 | 53 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 281–295 | 13 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 289–419 | 121 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 290–392 | 82 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 306–349 | 43 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 308–310 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 328–333 | 6 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 338–419 | 76 | 4 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 347–419 | 58 | 7 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 356–400 | 44 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 363–419 | 46 | 5 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 381–419 | 39 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 391–402 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (C): Annotated start 158 != Inferred start 162
- ⚠️ `Action_DownBlock` for actor_track_id `20` (C): Annotated start 161 != Inferred start 179
- ⚠️ `Action_DownBlock` for actor_track_id `20` (C): Annotated start 161 != Inferred start 179
- ❌ Missing segment for action `Action_DownBlock` on target `22` (RG)
- ❌ Missing segment for action `Action_PullBlock` on target `17` (LG)
- ❌ Missing segment for action `Action_PullLeadBlock` on target `4` (QB)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 659: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_PullLeadBlock' for track '3' has invalid range: start=161, end=157. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '16' has invalid range: start=161, end=88. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '18' has invalid range: start=161, end=76. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [158–171], lower_priority='Action_DownBlock' annotated_start=161, effective_Action_DownBlock_start=172.
- ⚠️ Segment 'Action_DownBlock' for track '21' has invalid range: start=161, end=68. Clamping end to start.
- ⚠️ Action 'Action_None' range [158-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-344] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-386] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [188-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-323] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-419] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-408] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '8' starts at frame 205, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [205-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-419] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-312] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-81] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-157] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-309] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-397] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-405] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-419] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-31] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-76] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-80] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-37] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-80] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-31] for track '18' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-74] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-126] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [162-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-48] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-80] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-92] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-31] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-68] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-358] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-366] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-384] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-398] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-387] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-413] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-360] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-382] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-370] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-378] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-388] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-367] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-397] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-381] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-419] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-419] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-402] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>