# Play-Annotation-Generator Annotation Review — PuntBlock_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_61`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 60
- **Ball Tracks:** 0
- **Action Segments:** 198
- **Validation Warnings:** 243
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 183
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Left_Guard | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Left_Guard | `10` | `10` | 14 | START | 14 | 41 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 40 | END | 40 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `12` | `12` | 60 | START | 60 | 111 |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | `2` | `2` | 73 | START | 73 | 78 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LongSnap` | 14 | 41 | 28 | inferred_complete_timeline |
| `Action_LongSnap` | 43 | 59 | 17 | inferred_complete_timeline |
| `Action_None` | 60 | 178 | 119 | inferred_complete_timeline |
| `Action_None` | 182 | 314 | 133 | inferred_complete_timeline |
| `Action_None` | 317 | 329 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 110 | 97 | inferred_complete_timeline |
| `Action_None` | 115 | 136 | 22 | inferred_complete_timeline |
| `Action_None` | 139 | 320 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 158 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 312 | 299 | inferred_complete_timeline |
| `Action_None` | 318 | 324 | 7 | inferred_complete_timeline |
| `Action_None` | 326 | 328 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 45 | 32 | inferred_complete_timeline |
| `Action_None` | 53 | 57 | 5 | inferred_complete_timeline |
| `Action_None` | 59 | 329 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 117 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 100 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 222 | 209 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 59 | 19 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 111 | 52 | inferred_complete_timeline |
| `Action_PuntBall` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_PuntBall` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PuntBall` | 138 | 144 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 121 | 108 | inferred_complete_timeline |
| `Action_None` | 127 | 151 | 25 | inferred_complete_timeline |
| `Action_None` | 156 | 164 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 90 | 104 | 15 | inferred_complete_timeline |
| `Action_None` | 106 | 119 | 14 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 54 | 41 | inferred_complete_timeline |
| `Action_None` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 150 | 88 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 197 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 110 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_None` | 54 | 67 | 14 | inferred_complete_timeline |
| `Action_None` | 71 | 115 | 45 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 148 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BlockPunt` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_None` | 79 | 168 | 90 | inferred_complete_timeline |
| `Action_None` | 199 | 246 | 48 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 171 | 158 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 219 | 43 | inferred_complete_timeline |
| `Action_None` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 329 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 115 | 102 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_None` | 48 | 128 | 81 | inferred_complete_timeline |
| `Action_None` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 170 | 157 | inferred_complete_timeline |
| `Action_None` | 193 | 196 | 4 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 34 | 21 | inferred_complete_timeline |
| `Action_None` | 37 | 74 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 17–25 | 7 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 21–99 | 75 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 40–48 | 9 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 88–114 | 25 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 97–109 | 8 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 111–245 | 72 | 5 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 120–329 | 128 | 8 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 128–235 | 71 | 4 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 158–177 | 13 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 159–329 | 145 | 10 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 162–181 | 10 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 165–329 | 165 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 166–329 | 161 | 4 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 167–304 | 82 | 7 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 176–286 | 72 | 5 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 183–237 | 55 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 186–298 | 97 | 10 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 202–329 | 128 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 218–329 | 112 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 222–315 | 59 | 5 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 267–302 | 36 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 268–317 | 45 | 2 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 293–329 | 33 | 4 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 310–313 | 4 | 1 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 312–315 | 4 | 1 | Undefined position; Undefined team |
| `53` | `82` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 319–320 | 2 | 1 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 321–329 | 9 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 321–329 | 8 | 2 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `58` | `87` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `12` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Jammer3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 163 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [14-34] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-74] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-136] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-168] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-222] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-219] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-54] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-158] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-312] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-128] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [14-41] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-178] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [60-111] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [113-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [127-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [131-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [138-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-117] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-100] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-148] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-48] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-219] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-229] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-322] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-242] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-283] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-179] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-288] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-230] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-237] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-205] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-247] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-298] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-292] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-302] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-315] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-299] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-302] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-317] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-302] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-329] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '58' has 1 frames without a visible bounding box.
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

</details>