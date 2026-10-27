# Play-Annotation-Generator Annotation Review — Counter_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_91`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 171
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 128
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 16 | START | 16 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 16 | START | 16 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 16 | START | 16 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 16 | START | 16 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 16 | START | 16 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 38 | START | 38 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 41 | START | 55 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 41 | START | 41 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `22` | `21` | 41 | START | 41 | 99 |
| ✅ EXACT | `Action_PullBlock` | LG | `20` | `19` | 41 | START | 41 | 91 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `9` | `8` | 41 | START | 41 | 79 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 49 | START | 49 | 87 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 54 | END | 38 | 54 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 66 | START | 66 | 87 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 88 | START | 88 | 225 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–247
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_None` | 55 | 65 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 66 | 87 | 22 | inferred_complete_timeline |
| `Action_None` | 88 | 247 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 16–225
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 49 | 87 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 225 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 16–251
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 237 | 200 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–300
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 237 | 200 | inferred_complete_timeline |
| `Action_None` | 239 | 279 | 41 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 16–260
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 260 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 16–264
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 61 | 24 | inferred_complete_timeline |
| `Action_None` | 66 | 79 | 14 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 102 | 12 | inferred_complete_timeline |
| `Action_None` | 105 | 204 | 100 | inferred_complete_timeline |
| `Action_None` | 209 | 217 | 9 | inferred_complete_timeline |
| `Action_None` | 219 | 230 | 12 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 264 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–79
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 41 | 79 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–91
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 41 | 91 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 16–243
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 110 | 47 | inferred_complete_timeline |
| `Action_None` | 111 | 243 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 16–108
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 41 | 83 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 108 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 16–113
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 41 | 99 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 107 | 7 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–127
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 97 | 60 | inferred_complete_timeline |
| `Action_None` | 102 | 127 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–251
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 129 | 92 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 251 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 16–68
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 68 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 16–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 242 | 205 | inferred_complete_timeline |
| `Action_None` | 244 | 249 | 6 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 268 | 10 | inferred_complete_timeline |
| `Action_None` | 270 | 282 | 13 | inferred_complete_timeline |
| `Action_None` | 287 | 297 | 11 | inferred_complete_timeline |
| `Action_None` | 299 | 303 | 5 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–249
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 90 | 53 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 142 | 33 | inferred_complete_timeline |
| `Action_None` | 145 | 226 | 82 | inferred_complete_timeline |
| `Action_None` | 229 | 237 | 9 | inferred_complete_timeline |
| `Action_None` | 242 | 249 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 16–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 266 | 229 | inferred_complete_timeline |
| `Action_None` | 270 | 284 | 15 | inferred_complete_timeline |
| `Action_None` | 287 | 292 | 6 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 329 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 16–324
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 321 | 284 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 237 | 200 | inferred_complete_timeline |
| `Action_None` | 242 | 264 | 23 | inferred_complete_timeline |
| `Action_None` | 266 | 329 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 16–321
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 279 | 242 | inferred_complete_timeline |
| `Action_None` | 289 | 304 | 16 | inferred_complete_timeline |
| `Action_None` | 306 | 321 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 16–293
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 207 | 170 | inferred_complete_timeline |
| `Action_None` | 209 | 264 | 56 | inferred_complete_timeline |
| `Action_None` | 280 | 293 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 16–306
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 277 | 240 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 287 | 306 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–279 | 209 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 76–175 | 78 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 77–191 | 109 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 80–81 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 96–221 | 117 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 121–329 | 198 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 142–329 | 185 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 145–318 | 163 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 182–185 | 4 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 190–256 | 51 | 4 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 193–211 | 10 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 199–266 | 64 | 4 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 278–291 | 14 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 293–329 | 36 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 312–329 | 18 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 312–329 | 12 | 3 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 313–329 | 14 | 3 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 319–329 | 6 | 2 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 319–324 | 5 | 2 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 119 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [38–54], lower_priority='Action_DownBlock' annotated_start=41, effective_Action_DownBlock_start=55.
- ⚠️ Action 'Action_None' range [38-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-279] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-142] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-226] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-321] for track '7' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [41-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-247] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-266] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-284] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-264] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-242] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-268] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-297] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-207] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-264] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-277] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-306] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-279] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-304] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-204] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-264] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [41-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [41-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [41-99] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-279] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-109] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-136] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-239] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-160] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-237] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-268] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-318] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-291] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '46' has 1 frames without a visible bounding box.
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