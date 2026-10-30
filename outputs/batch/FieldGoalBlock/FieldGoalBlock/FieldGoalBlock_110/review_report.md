# Play-Annotation-Generator Annotation Review — FieldGoalBlock_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_110`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 67
- **Ball Tracks:** 0
- **Action Segments:** 224
- **Validation Warnings:** 309
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 212
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `4` | `4` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher5 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `5` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `4` | `4` | 26 | START | 26 | 39 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 49 | START | 49 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher5 | `7` | `7` | 55 | START | 55 | 60 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PlaceBall` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 196 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_KickBall` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_None` | 56 | 236 | 181 | inferred_complete_timeline |
| `Action_None` | 241 | 312 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_None` | 87 | 117 | 31 | inferred_complete_timeline |
| `Action_None` | 123 | 135 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–512
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 72 | 24 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 146 | 28 | inferred_complete_timeline |
| `Action_None` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 171 | 13 | inferred_complete_timeline |
| `Action_None` | 174 | 512 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 129 | 81 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 66 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 114 | 66 | inferred_complete_timeline |
| `Action_None` | 116 | 173 | 58 | inferred_complete_timeline |
| `Action_None` | 185 | 205 | 21 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 218 | 221 | 4 | inferred_complete_timeline |
| `Action_None` | 230 | 274 | 45 | inferred_complete_timeline |
| `Action_None` | 279 | 352 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–463
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 122 | 64 | inferred_complete_timeline |
| `Action_None` | 125 | 219 | 95 | inferred_complete_timeline |
| `Action_None` | 224 | 463 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–531
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_None` | 71 | 147 | 77 | inferred_complete_timeline |
| `Action_None` | 149 | 531 | 383 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 148 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–517
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 162 | 114 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 517 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 11 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 48 | 30 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 25 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 30 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 629 | 463 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 54 | 20 | inferred_complete_timeline |
| `Action_BlockKick` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_BlockKick` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_BlockKick` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 151 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 207 | 159 | inferred_complete_timeline |
| `Action_None` | 225 | 229 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 629 | 398 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 48 | 31 | inferred_complete_timeline |
| `Action_None` | 49 | 160 | 112 | inferred_complete_timeline |
| `Action_None` | 176 | 251 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–182 | 118 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 5–92 | 86 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 16–135 | 68 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 20–465 | 414 | 8 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 22–629 | 592 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–345 | 289 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 102–128 | 7 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 115–170 | 54 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 125–495 | 332 | 7 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 144–171 | 18 | 5 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 169–522 | 345 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 194–199 | 6 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 196–512 | 294 | 8 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 196–256 | 51 | 4 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 198–628 | 421 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 202–259 | 58 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 213–510 | 297 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 219–267 | 35 | 4 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 233–257 | 25 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 249–277 | 29 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 256–290 | 35 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 264–268 | 5 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 264–277 | 14 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 271–479 | 206 | 3 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 279–298 | 20 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 300–310 | 11 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 301–302 | 2 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 304–489 | 186 | 1 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 305–307 | 3 | 1 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 309–310 | 2 | 1 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 313–316 | 4 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 314–528 | 209 | 3 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 327–531 | 205 | 1 | Undefined position; Undefined team |
| `51` | `76` | Position_Unknown | Team_Unknown | 351–504 | 154 | 1 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 370–507 | 84 | 13 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 379–452 | 73 | 2 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 386–387 | 2 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 402–458 | 57 | 1 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 426–526 | 100 | 2 | Undefined position; Undefined team |
| `58` | `87` | Position_Unknown | Team_Unknown | 468–570 | 95 | 4 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 496–504 | 5 | 2 | Undefined position; Undefined team |
| `60` | `94` | Position_Unknown | Team_Unknown | 515–597 | 7 | 2 | Undefined position; Undefined team |
| `61` | `95` | Position_Unknown | Team_Unknown | 542–561 | 19 | 2 | Undefined position; Undefined team |
| `62` | `96` | Position_Unknown | Team_Unknown | 548–557 | 9 | 2 | Undefined position; Undefined team |
| `63` | `97` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `64` | `99` | Position_Unknown | Team_Unknown | 555–559 | 5 | 1 | Undefined position; Undefined team |
| `65` | `102` | Position_Unknown | Team_Unknown | 566–567 | 2 | 1 | Undefined position; Undefined team |
| `66` | `104` | Position_Unknown | Team_Unknown | 589–590 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 50 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 50 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 100 |
| Missing visible bounding boxes during action | 207 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [56-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-312] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-45] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-166] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-207] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-629] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-148] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-196] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-146] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-512] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-162] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-517] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [55-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [62-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-173] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-205] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-274] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-352] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-147] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-531] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-251] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-66] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-219] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-463] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-629] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-11] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-87] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-48] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-29] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-80] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-128] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-203] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-465] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-480] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-629] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-345] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-131] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-170] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-350] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-495] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-285] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-522] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-357] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-385] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-391] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-403] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-512] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-620] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-628] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-510] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-267] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-257] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-277] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-277] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-298] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-479] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-298] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-489] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-400] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-528] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-531] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-504] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-448] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-463] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-473] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-488] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-507] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-448] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-458] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-526] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-542] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-559] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-566] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-570] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-504] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-519] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-549] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-561] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-552] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-559] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>