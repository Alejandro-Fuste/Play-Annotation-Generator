# Play-Annotation-Generator Annotation Review — PuntBlock_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_41`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 509
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 193
- **Validation Warnings:** 235
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 175
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Personal_Protector3 | offense | `13` | `13` |
| ✅ EXACT | `Action_SecureRecovery` | Right_Jammer3 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | `20` | `20` | 12 | START | 12 | 71 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 245 | END | 245 | 245 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 266 | START | 266 | 267 |
| ⚠️ START CHANGED | `Action_BlockPunt` | Personal_Protector3 | `13` | `13` | 267 | START | 268 | 274 |
| ✅ EXACT | `Action_SecureRecovery` | Right_Jammer3 | `14` | `14` | 439 | START | 439 | 453 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_LongSnap` | 12 | 71 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 102 | 91 | inferred_complete_timeline |
| `Action_None` | 105 | 125 | 21 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 509 | 498 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 46 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 509 | 498 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 143 | 132 | inferred_complete_timeline |
| `Action_None` | 145 | 476 | 332 | inferred_complete_timeline |
| `Action_None` | 478 | 509 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 114 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 266 | 143 | inferred_complete_timeline |
| `Action_BlockPunt` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 275 | 509 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_SnapReceive` | 245 | 245 | 1 | inferred_complete_timeline |
| `Action_None` | 246 | 265 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 90 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 39 | 28 | inferred_complete_timeline |
| `Action_None` | 42 | 91 | 50 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 94 | 83 | inferred_complete_timeline |
| `Action_None` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 137 | 126 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 231 | 66 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 275 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 509 | 498 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 230 | 219 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 258 | 17 | inferred_complete_timeline |
| `Action_None` | 263 | 307 | 45 | inferred_complete_timeline |
| `Action_None` | 309 | 509 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_None` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_None` | 66 | 72 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 51 | 40 | inferred_complete_timeline |
| `Action_None` | 53 | 110 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 55 | 44 | inferred_complete_timeline |
| `Action_None` | 57 | 84 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–506
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 292 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 355 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 438 | 81 | inferred_complete_timeline |
| `Action_SecureRecovery` | 439 | 453 | 15 | inferred_complete_timeline |
| `Action_None` | 454 | 498 | 45 | inferred_complete_timeline |
| `Action_None` | 500 | 501 | 2 | inferred_complete_timeline |
| `Action_None` | 503 | 506 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_None` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_None` | 154 | 288 | 135 | inferred_complete_timeline |
| `Action_None` | 290 | 297 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_None` | 129 | 369 | 241 | inferred_complete_timeline |
| `Action_None` | 373 | 376 | 4 | inferred_complete_timeline |
| `Action_None` | 380 | 509 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 37–419 | 290 | 25 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 51–509 | 428 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 74–85 | 5 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 93–107 | 10 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 97–183 | 84 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 99–262 | 151 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 108–115 | 8 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 118–123 | 6 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 121–130 | 10 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 122–126 | 5 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 137–172 | 20 | 7 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 145–151 | 6 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 151–229 | 49 | 5 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 160–400 | 241 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 213–243 | 23 | 5 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 267–509 | 242 | 2 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 268–270 | 3 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 270–376 | 41 | 7 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 287–291 | 5 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 302–509 | 208 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 304–509 | 206 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 304–509 | 195 | 3 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 309–509 | 201 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 341–509 | 159 | 4 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 408–509 | 94 | 4 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 410–440 | 15 | 4 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 418–509 | 92 | 1 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 429–509 | 77 | 2 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 442–455 | 14 | 1 | Undefined position; Undefined team |
| `55` | `75` | Position_Unknown | Team_Unknown | 494–500 | 6 | 2 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 503–509 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockPunt` for actor_track_id `13` (Personal_Protector3): Annotated start 267 != Inferred start 268

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Jammer5` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Jammer4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Guard` position mapped to `offense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 160 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 84: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [12-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-509] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-230] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-509] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-84] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-369] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-137] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-275] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [266-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-114] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-266] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-355] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-498] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-506] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-91] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-288] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-143] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-476] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [12-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-54] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-71] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-122] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-173] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-328] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-389] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-405] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-365] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-499] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-186] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-400] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-460] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-509] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-352] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-370] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-299] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-509] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-483] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-494] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-355] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-436] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-463] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-471] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-492] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-509] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-424] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-470] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-455] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '55' has 1 frames without a visible bounding box.
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

</details>