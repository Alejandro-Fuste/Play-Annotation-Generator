# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_101`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 85
- **Ball Tracks:** 0
- **Action Segments:** 387
- **Validation Warnings:** 489
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 371
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `68` | `41` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `68` | `41` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `109` | `65` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `11` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `18` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `19` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 8 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 8 | START | 8 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 8 | START | 8 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 8 | START | 8 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `8` | `8` | 23 | START | 23 | 44 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 72 | START | 72 | 88 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `68` | `41` | 206 | START | 206 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `68` | `41` | 228 | START | 228 | 302 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `109` | `65` | 600 | START | 604 | 605 |

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
- **Visible Frames:** 8–96
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 53 | 31 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 89 | 26 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 8–627
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 104 | 82 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 129 | 17 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_None` | 142 | 200 | 59 | inferred_complete_timeline |
| `Action_None` | 202 | 321 | 120 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |
| `Action_None` | 328 | 538 | 211 | inferred_complete_timeline |
| `Action_None` | 540 | 543 | 4 | inferred_complete_timeline |
| `Action_None` | 548 | 553 | 6 | inferred_complete_timeline |
| `Action_None` | 597 | 598 | 2 | inferred_complete_timeline |
| `Action_None` | 600 | 601 | 2 | inferred_complete_timeline |
| `Action_None` | 603 | 607 | 5 | inferred_complete_timeline |
| `Action_None` | 609 | 617 | 9 | inferred_complete_timeline |
| `Action_None` | 619 | 627 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 34–128
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 34 | 44 | 11 | inferred_complete_timeline |
| `Action_None` | 46 | 90 | 45 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–237
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 51 | 29 | inferred_complete_timeline |
| `Action_None` | 60 | 162 | 103 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 8–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_LongSnap` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 47 | 71 | 25 | inferred_complete_timeline |
| `Action_None` | 72 | 629 | 558 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 8–97
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 97 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–121
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 49 | 27 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–275
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 79 | 57 | inferred_complete_timeline |
| `Action_None` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 218 | 93 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 262 | 15 | inferred_complete_timeline |
| `Action_None` | 270 | 275 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–169
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 72 | 88 | 17 | inferred_complete_timeline |
| `Action_None` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 107 | 169 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–164
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 50 | 28 | inferred_complete_timeline |
| `Action_None` | 52 | 164 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–150
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 8–126
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 98 | 76 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–97
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 57 | 35 | inferred_complete_timeline |
| `Action_None` | 59 | 89 | 31 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 8–111
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 38 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–96
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 74 | 52 | inferred_complete_timeline |
| `Action_None` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–321
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 174 | 152 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 207 | 19 | inferred_complete_timeline |
| `Action_None` | 214 | 241 | 28 | inferred_complete_timeline |
| `Action_None` | 243 | 283 | 41 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–109
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 109 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 8–90
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 90 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–81
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 68 | 46 | inferred_complete_timeline |
| `Action_None` | 71 | 81 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–91
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 36 | 14 | inferred_complete_timeline |
| `Action_None` | 38 | 53 | 16 | inferred_complete_timeline |
| `Action_None` | 55 | 91 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 8–619 | 551 | 17 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 54–337 | 176 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 74–143 | 69 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 86–96 | 4 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 87–207 | 83 | 8 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 93–391 | 275 | 10 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 95–464 | 353 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 117–271 | 133 | 8 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 138–384 | 198 | 10 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 138–150 | 13 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 165–319 | 97 | 10 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 166–629 | 444 | 7 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 171–390 | 216 | 4 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 174–626 | 398 | 10 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 174–267 | 82 | 5 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 175–277 | 103 | 1 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 183–495 | 206 | 17 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 188–400 | 199 | 12 | Undefined position; Undefined team |
| `42` | `70` | Position_Unknown | Team_Unknown | 220–247 | 19 | 3 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 235–396 | 162 | 1 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `46` | `76` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `47` | `79` | Position_Unknown | Team_Unknown | 256–257 | 2 | 1 | Undefined position; Undefined team |
| `48` | `80` | Position_Unknown | Team_Unknown | 256–451 | 154 | 7 | Undefined position; Undefined team |
| `49` | `81` | Position_Unknown | Team_Unknown | 256–258 | 3 | 1 | Undefined position; Undefined team |
| `50` | `82` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `51` | `83` | Position_Unknown | Team_Unknown | 266–384 | 115 | 3 | Undefined position; Undefined team |
| `52` | `85` | Position_Unknown | Team_Unknown | 277–335 | 46 | 6 | Undefined position; Undefined team |
| `53` | `87` | Position_Unknown | Team_Unknown | 279–314 | 35 | 2 | Undefined position; Undefined team |
| `54` | `88` | Position_Unknown | Team_Unknown | 280–448 | 161 | 6 | Undefined position; Undefined team |
| `55` | `91` | Position_Unknown | Team_Unknown | 291–317 | 24 | 3 | Undefined position; Undefined team |
| `56` | `92` | Position_Unknown | Team_Unknown | 291–460 | 154 | 9 | Undefined position; Undefined team |
| `57` | `94` | Position_Unknown | Team_Unknown | 316–318 | 3 | 1 | Undefined position; Undefined team |
| `58` | `95` | Position_Unknown | Team_Unknown | 326–627 | 223 | 11 | Undefined position; Undefined team |
| `59` | `96` | Position_Unknown | Team_Unknown | 326–410 | 81 | 2 | Undefined position; Undefined team |
| `60` | `99` | Position_Unknown | Team_Unknown | 353–519 | 129 | 8 | Undefined position; Undefined team |
| `61` | `100` | Position_Unknown | Team_Unknown | 371–546 | 158 | 5 | Undefined position; Undefined team |
| `62` | `102` | Position_Unknown | Team_Unknown | 373–537 | 149 | 4 | Undefined position; Undefined team |
| `63` | `103` | Position_Unknown | Team_Unknown | 384–423 | 39 | 2 | Undefined position; Undefined team |
| `64` | `107` | Position_Unknown | Team_Unknown | 400–556 | 35 | 6 | Undefined position; Undefined team |
| `65` | `109` | Position_Unknown | Team_Unknown | 421–627 | 53 | 16 | Undefined position; Undefined team |
| `66` | `110` | Position_Unknown | Team_Unknown | 427–451 | 5 | 2 | Undefined position; Undefined team |
| `67` | `111` | Position_Unknown | Team_Unknown | 431–467 | 26 | 6 | Undefined position; Undefined team |
| `68` | `114` | Position_Unknown | Team_Unknown | 443–469 | 21 | 3 | Undefined position; Undefined team |
| `69` | `116` | Position_Unknown | Team_Unknown | 448–452 | 5 | 1 | Undefined position; Undefined team |
| `70` | `123` | Position_Unknown | Team_Unknown | 473–574 | 65 | 11 | Undefined position; Undefined team |
| `71` | `124` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `72` | `126` | Position_Unknown | Team_Unknown | 485–490 | 5 | 2 | Undefined position; Undefined team |
| `73` | `128` | Position_Unknown | Team_Unknown | 501–525 | 25 | 1 | Undefined position; Undefined team |
| `74` | `130` | Position_Unknown | Team_Unknown | 539–540 | 2 | 1 | Undefined position; Undefined team |
| `75` | `131` | Position_Unknown | Team_Unknown | 539–551 | 5 | 2 | Undefined position; Undefined team |
| `76` | `133` | Position_Unknown | Team_Unknown | 544–545 | 2 | 1 | Undefined position; Undefined team |
| `77` | `134` | Position_Unknown | Team_Unknown | 545–626 | 37 | 9 | Undefined position; Undefined team |
| `78` | `136` | Position_Unknown | Team_Unknown | 552–568 | 15 | 2 | Undefined position; Undefined team |
| `79` | `138` | Position_Unknown | Team_Unknown | 564–567 | 4 | 1 | Undefined position; Undefined team |
| `80` | `139` | Position_Unknown | Team_Unknown | 594–595 | 2 | 1 | Undefined position; Undefined team |
| `81` | `141` | Position_Unknown | Team_Unknown | 610–629 | 17 | 2 | Undefined position; Undefined team |
| `82` | `142` | Position_Unknown | Team_Unknown | 613–614 | 2 | 1 | Undefined position; Undefined team |
| `83` | `144` | Position_Unknown | Team_Unknown | 627–629 | 3 | 1 | Undefined position; Undefined team |
| `84` | `145` | Position_Unknown | Team_Unknown | 629–629 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `68` (9 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `109` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 65 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 65 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 130 |
| Missing visible bounding boxes during action | 356 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [23-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-90] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-68] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-74] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-218] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-262] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-57] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-89] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-174] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-207] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-241] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-283] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [72-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-104] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-169] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [23-44] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-281] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-321] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-359] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-407] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-541] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-547] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-572] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-585] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-598] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-611] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-619] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-104] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-129] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-538] for track '11' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-553] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-607] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-617] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-627] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-53] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-89] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-38] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-162] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-44] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-223] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-337] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-98] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-132] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-185] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-207] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-110] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-304] for track '25' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-317] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-337] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-352] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-391] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-138] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-300] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-464] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-192] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-250] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-211] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-312] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-363] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-197] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-245] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-267] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-319] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-193] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-338] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-513] for track '34' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-302] for track '36' has 11 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-390] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-190] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-283] for track '37' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-355] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-481] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-490] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-626] for track '37' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-230] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-250] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-277] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-259] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-287] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-321] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-405] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-418] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-429] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-454] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-487] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-495] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-302] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [307-331] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [333-340] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [342-345] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [348-365] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [367-370] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [372-391] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [393-394] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [398-400] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-232] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-396] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-265] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-285] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-321] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-339] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-353] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-377] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-451] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-272] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-379] for track '51' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-317] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-327] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-314] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-418] for track '54' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-428] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-434] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-445] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-317] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-322] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-365] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-399] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-408] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-457] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-336] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-488] for track '58' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-530] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-535] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-565] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-609] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-627] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-402] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-390] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-475] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-494] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-506] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-403] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-418] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-508] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-522] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-546] for track '61' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-397] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-418] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-447] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-537] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-423] for track '63' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-419] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-456] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-472] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-423] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-449] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-457] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-467] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-503] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-533] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [538-539] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [545-546] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [554-557] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [587-589] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [593-595] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [604-605] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [607-614] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '65' starts at frame 619, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [619-619] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-443] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-449] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-460] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-469] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-452] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-479] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-497] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-528] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-548] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-558] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-564] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-574] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-525] for track '73' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-551] for track '77' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-562] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-570] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-594] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-609] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-618] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-564] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-567] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-613] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>