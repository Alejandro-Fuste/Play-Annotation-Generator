# Play-Annotation-Generator Annotation Review — PuntBlock_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_83`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 117
- **Ball Tracks:** 0
- **Action Segments:** 239
- **Validation Warnings:** 402
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 224
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Jammer2 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `17` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 14 | START | 14 | 36 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 42 | END | 42 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `9` | `9` | 75 | START | 75 | 223 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `21` | `21` | 86 | START | 86 | 95 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Jammer2 | `2` | `2` | 305 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 264 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 243 | 230 | inferred_complete_timeline |
| `Action_None` | 246 | 264 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 108 | 95 | inferred_complete_timeline |
| `Action_None` | 110 | 231 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LongSnap` | 14 | 36 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 188 | 175 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 253 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 97 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 74 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 75 | 223 | 149 | inferred_complete_timeline |
| `Action_PuntBall` | 228 | 229 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 278 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 207 | 194 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 264 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 52 | 39 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 194 | 181 | inferred_complete_timeline |
| `Action_None` | 196 | 203 | 8 | inferred_complete_timeline |
| `Action_None` | 207 | 218 | 12 | inferred_complete_timeline |
| `Action_None` | 220 | 225 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 42 | 29 | inferred_complete_timeline |
| `Action_None` | 50 | 243 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 81 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 121 | 108 | inferred_complete_timeline |
| `Action_None` | 125 | 131 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 232 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 194 | 181 | inferred_complete_timeline |
| `Action_None` | 196 | 229 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 17 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 144 | 131 | inferred_complete_timeline |
| `Action_None` | 149 | 223 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 68 | 55 | inferred_complete_timeline |
| `Action_None` | 76 | 180 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 77 | 64 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 89 | 147 | 59 | inferred_complete_timeline |
| `Action_None` | 203 | 263 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 33–245 | 176 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 44–287 | 235 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 54–92 | 25 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 66–231 | 166 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 107–230 | 124 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 107–223 | 116 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 109–160 | 16 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 110–132 | 22 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 137–154 | 18 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 139–264 | 112 | 6 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 156–204 | 49 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 159–185 | 23 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 161–224 | 64 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 163–202 | 15 | 3 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 169–230 | 55 | 3 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 173–224 | 45 | 5 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 194–266 | 15 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 213–224 | 7 | 3 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 221–264 | 44 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 221–259 | 37 | 3 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 230–240 | 11 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 231–252 | 14 | 3 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 239–247 | 9 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 239–241 | 3 | 1 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 244–252 | 9 | 1 | Undefined position; Undefined team |
| `54` | `74` | Position_Unknown | Team_Unknown | 252–261 | 9 | 2 | Undefined position; Undefined team |
| `55` | `75` | Position_Unknown | Team_Unknown | 253–272 | 11 | 4 | Undefined position; Undefined team |
| `56` | `78` | Position_Unknown | Team_Unknown | 257–260 | 4 | 1 | Undefined position; Undefined team |
| `57` | `79` | Position_Unknown | Team_Unknown | 261–264 | 4 | 1 | Undefined position; Undefined team |
| `58` | `80` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 265–274 | 10 | 1 | Undefined position; Undefined team |
| `60` | `84` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `61` | `85` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `62` | `86` | Position_Unknown | Team_Unknown | 265–274 | 5 | 2 | Undefined position; Undefined team |
| `63` | `87` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `64` | `88` | Position_Unknown | Team_Unknown | 267–278 | 5 | 2 | Undefined position; Undefined team |
| `65` | `89` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `66` | `90` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `67` | `91` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `68` | `93` | Position_Unknown | Team_Unknown | 269–272 | 4 | 1 | Undefined position; Undefined team |
| `69` | `94` | Position_Unknown | Team_Unknown | 269–280 | 7 | 2 | Undefined position; Undefined team |
| `70` | `95` | Position_Unknown | Team_Unknown | 269–272 | 4 | 1 | Undefined position; Undefined team |
| `71` | `96` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `72` | `97` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `73` | `98` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `74` | `99` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `75` | `107` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `76` | `108` | Position_Unknown | Team_Unknown | 273–298 | 16 | 2 | Undefined position; Undefined team |
| `77` | `109` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `78` | `110` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `79` | `111` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `80` | `112` | Position_Unknown | Team_Unknown | 273–298 | 6 | 2 | Undefined position; Undefined team |
| `81` | `113` | Position_Unknown | Team_Unknown | 273–389 | 80 | 4 | Undefined position; Undefined team |
| `82` | `114` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `83` | `115` | Position_Unknown | Team_Unknown | 275–389 | 113 | 2 | Undefined position; Undefined team |
| `84` | `116` | Position_Unknown | Team_Unknown | 275–285 | 11 | 1 | Undefined position; Undefined team |
| `85` | `117` | Position_Unknown | Team_Unknown | 275–389 | 108 | 5 | Undefined position; Undefined team |
| `86` | `118` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `87` | `119` | Position_Unknown | Team_Unknown | 275–276 | 2 | 1 | Undefined position; Undefined team |
| `88` | `120` | Position_Unknown | Team_Unknown | 275–300 | 25 | 2 | Undefined position; Undefined team |
| `89` | `121` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `90` | `122` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `91` | `123` | Position_Unknown | Team_Unknown | 277–295 | 19 | 1 | Undefined position; Undefined team |
| `92` | `124` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `93` | `125` | Position_Unknown | Team_Unknown | 279–295 | 15 | 3 | Undefined position; Undefined team |
| `94` | `126` | Position_Unknown | Team_Unknown | 279–293 | 5 | 2 | Undefined position; Undefined team |
| `95` | `127` | Position_Unknown | Team_Unknown | 281–295 | 15 | 1 | Undefined position; Undefined team |
| `96` | `128` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `97` | `134` | Position_Unknown | Team_Unknown | 286–293 | 8 | 1 | Undefined position; Undefined team |
| `98` | `135` | Position_Unknown | Team_Unknown | 286–389 | 104 | 1 | Undefined position; Undefined team |
| `99` | `136` | Position_Unknown | Team_Unknown | 288–290 | 3 | 1 | Undefined position; Undefined team |
| `100` | `137` | Position_Unknown | Team_Unknown | 289–389 | 43 | 7 | Undefined position; Undefined team |
| `101` | `139` | Position_Unknown | Team_Unknown | 296–298 | 3 | 1 | Undefined position; Undefined team |
| `102` | `140` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `103` | `141` | Position_Unknown | Team_Unknown | 299–309 | 11 | 1 | Undefined position; Undefined team |
| `104` | `144` | Position_Unknown | Team_Unknown | 305–389 | 73 | 3 | Undefined position; Undefined team |
| `105` | `147` | Position_Unknown | Team_Unknown | 310–389 | 80 | 1 | Undefined position; Undefined team |
| `106` | `148` | Position_Unknown | Team_Unknown | 310–313 | 4 | 1 | Undefined position; Undefined team |
| `107` | `151` | Position_Unknown | Team_Unknown | 322–389 | 63 | 5 | Undefined position; Undefined team |
| `108` | `152` | Position_Unknown | Team_Unknown | 324–389 | 51 | 5 | Undefined position; Undefined team |
| `109` | `154` | Position_Unknown | Team_Unknown | 327–374 | 33 | 5 | Undefined position; Undefined team |
| `110` | `155` | Position_Unknown | Team_Unknown | 332–353 | 17 | 3 | Undefined position; Undefined team |
| `111` | `156` | Position_Unknown | Team_Unknown | 342–389 | 48 | 1 | Undefined position; Undefined team |
| `112` | `159` | Position_Unknown | Team_Unknown | 377–389 | 13 | 1 | Undefined position; Undefined team |
| `113` | `160` | Position_Unknown | Team_Unknown | 382–384 | 3 | 1 | Undefined position; Undefined team |
| `114` | `162` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `115` | `163` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |
| `116` | `164` | Position_Unknown | Team_Unknown | 386–389 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `2` (Left_Jammer2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 96 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 96 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 192 |
| Missing visible bounding boxes during action | 206 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 168: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '2' has invalid range: start=305, end=232. Clamping end to start.
- ⚠️ Action 'Action_None' range [14-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-232] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-264] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-108] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-231] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [75-223] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [228-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-68] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-97] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-194] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [14-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-42] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-243] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-17] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-188] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-253] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-52] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [86-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-276] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-92] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-231] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-230] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-154] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-179] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-214] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-229] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-204] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-224] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-188] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-230] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-209] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-264] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-253] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-240] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-298] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-293] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-389] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-364] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-295] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-334] for track '85' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-360] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-389] for track '85' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-300] for track '88' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-295] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '92' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '93' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '94' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-295] for track '95' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '96' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '97' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '99' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-374] for track '100' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-386] for track '100' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '101' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '102' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-309] for track '103' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-317] for track '104' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-342] for track '104' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '106' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '107' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '107' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-385] for track '107' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-332] for track '108' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-363] for track '108' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-372] for track '108' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-336] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '109' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-353] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '109' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-343] for track '110' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '110' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-389] for track '111' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-389] for track '112' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '113' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '92' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '92' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '93' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '93' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '94' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '94' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '95' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '95' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '96' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '96' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '97' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '97' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '98' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '98' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '99' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '99' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '100' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '100' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '101' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '101' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '102' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '102' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '103' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '103' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '104' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '104' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '105' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '105' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '106' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '106' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '107' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '107' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '108' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '108' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '109' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '109' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '110' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '110' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '111' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '111' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '112' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '112' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '113' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '113' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '114' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '114' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '115' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '115' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '116' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '116' has undefined team_side. Will map to Team_Unknown.

</details>