# Play-Annotation-Generator Annotation Review — PuntCoverage_59

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_59`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 209
- **Validation Warnings:** 262
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 168
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `8` | `Group` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `26` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 8 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 18 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 41 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `4` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `8` | `Group` | 0 | START | 0 | 135 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 72 | START | 72 | 87 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `26` | `25` | 206 | START | 206 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `26` | `25` | 228 | START | 228 | 274 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 18–124
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 82 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 124 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–32
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 19 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 50 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 62 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 181 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 300 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 93 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 137 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PuntBall` | 72 | 87 | 16 | inferred_complete_timeline |
| `Action_None` | 88 | 324 | 237 | inferred_complete_timeline |
| `Action_None` | 336 | 509 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 41–112
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 93 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 112 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 208 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 244 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 269 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 286 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 353 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 365 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 509 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 142 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 315 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 509 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 50 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 99 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 482 | 375 | inferred_complete_timeline |
| `Action_PreSnap` | 490 | 492 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 496 | 497 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 500 | 509 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 99 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 106 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 97 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 120 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 50 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 368 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 106 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 442 | 332 | inferred_complete_timeline |
| `Action_PreSnap` | 445 | 446 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 130 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 362 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 509 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–48 | 49 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–509 | 498 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 46–246 | 101 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 64–509 | 413 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 79–110 | 24 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 83–142 | 49 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 126–322 | 181 | 8 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 142–256 | 111 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 146–509 | 325 | 10 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 147–224 | 76 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 148–230 | 70 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 157–509 | 228 | 9 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 170–286 | 109 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 172–209 | 33 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 181–275 | 88 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 187–458 | 251 | 5 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 207–266 | 34 | 4 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 222–477 | 191 | 5 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 253–320 | 68 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 258–496 | 217 | 6 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 277–320 | 44 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 285–509 | 202 | 6 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 292–425 | 68 | 6 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 301–333 | 33 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 304–509 | 206 | 1 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 308–426 | 117 | 3 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 318–485 | 168 | 1 | Undefined position; Undefined team |
| `46` | `53` | Position_Unknown | Team_Unknown | 336–504 | 156 | 2 | Undefined position; Undefined team |
| `47` | `55` | Position_Unknown | Team_Unknown | 348–421 | 73 | 2 | Undefined position; Undefined team |
| `48` | `57` | Position_Unknown | Team_Unknown | 354–417 | 64 | 1 | Undefined position; Undefined team |
| `49` | `59` | Position_Unknown | Team_Unknown | 411–450 | 30 | 3 | Undefined position; Undefined team |
| `50` | `60` | Position_Unknown | Team_Unknown | 450–455 | 5 | 2 | Undefined position; Undefined team |
| `51` | `62` | Position_Unknown | Team_Unknown | 482–493 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `26` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 61, Column 'Tackle': Unknown actor track ID '?' in entry '477,501,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 194 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 120: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_None' range [88-324] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-368] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-48] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-105] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-509] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-130] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-362] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-50] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-74] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-99] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-482] for track '7' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [490-492] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [496-497] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-353] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-365] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-50] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-106] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-442] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-446] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-97] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-54] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-137] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-99] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-50] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-19] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-82] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-93] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-93] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-71] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-246] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-257] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-269] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-358] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-384] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-400] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-99] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-132] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-274] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-307] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-311] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [319-322] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-233] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-243] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-284] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-442] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-482] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-493] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-504] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-186] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-230] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-378] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-383] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-469] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-483] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-216] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-262] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-286] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-222] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-200] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-283] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-335] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-430] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-458] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-229] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-386] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-423] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-431] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-477] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-320] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-402] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-421] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-450] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-461] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-469] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-496] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-320] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-433] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-442] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-490] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-504] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-322] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-356] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-385] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-425] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-351] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-362] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-426] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-485] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-487] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-504] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-366] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-421] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-417] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-422] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-450] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-452] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-455] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-493] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.

</details>