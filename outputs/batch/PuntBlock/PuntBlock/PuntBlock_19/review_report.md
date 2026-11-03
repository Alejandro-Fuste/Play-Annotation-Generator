# Play-Annotation-Generator Annotation Review — PuntBlock_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_19`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 175
- **Validation Warnings:** 219
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 160
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Right_Tackle | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | defense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `7` | `7` | 10 | START | 10 | 61 |
| ✅ EXACT | `Action_SnapReceive` | Right_Tackle | `3` | `3` | 40 | END | 40 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `13` | `13` | 62 | START | 62 | 168 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | `19` | `19` | 80 | START | 80 | 83 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 66 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 55 | 46 | inferred_complete_timeline |
| `Action_None` | 61 | 124 | 64 | inferred_complete_timeline |
| `Action_None` | 126 | 138 | 13 | inferred_complete_timeline |
| `Action_None` | 181 | 207 | 27 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 150 | 141 | inferred_complete_timeline |
| `Action_None` | 153 | 234 | 82 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 267 | 288 | 22 | inferred_complete_timeline |
| `Action_None` | 290 | 295 | 6 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 257 | 248 | inferred_complete_timeline |
| `Action_None` | 267 | 321 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 73 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PuntBall` | 62 | 168 | 107 | inferred_complete_timeline |
| `Action_PuntBall` | 177 | 287 | 111 | inferred_complete_timeline |
| `Action_PuntBall` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_PuntBall` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_LongSnap` | 10 | 61 | 52 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 237 | 197 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |
| `Action_None` | 254 | 267 | 14 | inferred_complete_timeline |
| `Action_None` | 269 | 329 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 18 | 26 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_BlockPunt` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 329 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_None` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_None` | 57 | 329 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 34 | 25 | inferred_complete_timeline |
| `Action_None` | 36 | 131 | 96 | inferred_complete_timeline |
| `Action_None` | 141 | 162 | 22 | inferred_complete_timeline |
| `Action_None` | 164 | 187 | 24 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 310 | 105 | inferred_complete_timeline |
| `Action_None` | 322 | 324 | 3 | inferred_complete_timeline |
| `Action_None` | 326 | 328 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 113 | 104 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_None` | 146 | 255 | 110 | inferred_complete_timeline |
| `Action_None` | 257 | 329 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 66 | 57 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |
| `Action_None` | 213 | 224 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 260 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 96 | 87 | inferred_complete_timeline |
| `Action_None` | 107 | 210 | 104 | inferred_complete_timeline |
| `Action_None` | 214 | 329 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–127 | 77 | 12 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 19–22 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 45–311 | 257 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 70–71 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 73–329 | 249 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 87–90 | 4 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 90–329 | 222 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 106–118 | 12 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 107–136 | 23 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 112–124 | 13 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 114–155 | 39 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 125–137 | 10 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 129–146 | 11 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 140–175 | 19 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 149–329 | 176 | 4 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 152–281 | 48 | 5 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 161–232 | 46 | 4 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 173–242 | 7 | 3 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 175–216 | 33 | 4 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 192–228 | 28 | 3 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 202–228 | 22 | 3 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 227–255 | 5 | 2 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 240–270 | 22 | 4 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 243–247 | 5 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 246–257 | 12 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 246–329 | 83 | 2 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 254–256 | 3 | 1 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 276–329 | 54 | 1 | Undefined position; Undefined team |
| `57` | `76` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `58` | `77` | Position_Unknown | Team_Unknown | 301–302 | 2 | 1 | Undefined position; Undefined team |
| `59` | `82` | Position_Unknown | Team_Unknown | 324–328 | 5 | 1 | Undefined position; Undefined team |
| `60` | `83` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `13` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 137 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [10-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-96] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-113] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [10-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-124] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-207] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-150] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-234] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-187] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-310] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [62-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [177-287] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [294-299] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [305-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-66] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-257] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-321] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-47] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-11] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-50] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-63] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-22] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-201] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-302] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-169] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-136] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-122] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-143] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-155] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-267] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-283] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-276] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-197] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-199] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-212] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-203] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-222] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-216] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-228] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-256] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '60' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.

</details>