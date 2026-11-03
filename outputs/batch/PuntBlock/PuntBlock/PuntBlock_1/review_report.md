# Play-Annotation-Generator Annotation Review — PuntBlock_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_1`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 89
- **Ball Tracks:** 0
- **Action Segments:** 294
- **Validation Warnings:** 403
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 280
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | defense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Gunner | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `17` | `17` | 1 | START | 1 | 46 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `16` | `16` | 27 | END | 27 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `16` | `16` | 48 | START | 48 | 78 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher3 | `18` | `18` | 63 | START | 63 | 69 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Gunner | `7` | `7` | 233 | START | N/A | N/A |

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
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 45 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 167 | 167 | inferred_complete_timeline |
| `Action_None` | 175 | 202 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 22 | 22 | inferred_complete_timeline |
| `Action_None` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_None` | 56 | 64 | 9 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 122 | 10 | inferred_complete_timeline |
| `Action_None` | 124 | 132 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 169 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 46 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 46 | 46 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 51 | 51 | inferred_complete_timeline |
| `Action_None` | 58 | 100 | 43 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 172 | 57 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |
| `Action_None` | 229 | 278 | 50 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 47 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 48 | 78 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_PuntBall` | 126 | 130 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 27 | 27 | inferred_complete_timeline |
| `Action_None` | 30 | 75 | 46 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 30 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |
| `Action_None` | 50 | 69 | 20 | inferred_complete_timeline |
| `Action_None` | 71 | 91 | 21 | inferred_complete_timeline |
| `Action_None` | 93 | 146 | 54 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 282 | 19 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 45 | 45 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 62 | 10 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 194 | 124 | inferred_complete_timeline |
| `Action_None` | 196 | 212 | 17 | inferred_complete_timeline |
| `Action_None` | 214 | 254 | 41 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_BlockPunt` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 132 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 212 | 212 | inferred_complete_timeline |
| `Action_None` | 218 | 284 | 67 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_None` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 113 | 134 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 280 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 94 | 94 | inferred_complete_timeline |
| `Action_None` | 108 | 129 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 66 | 66 | inferred_complete_timeline |
| `Action_None` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 51 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–56 | 57 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 41–44 | 4 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 50–223 | 164 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 55–133 | 79 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 59–68 | 10 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 59–197 | 71 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 70–79 | 5 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 72–175 | 81 | 8 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 89–243 | 34 | 6 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 90–99 | 6 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 92–281 | 169 | 6 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 96–100 | 5 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 96–245 | 21 | 7 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 97–280 | 164 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 100–109 | 5 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 104–136 | 33 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 109–299 | 191 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 122–123 | 2 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 128–170 | 23 | 3 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 128–132 | 5 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 130–229 | 75 | 6 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 135–152 | 18 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 137–194 | 29 | 7 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 149–159 | 7 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 152–299 | 144 | 3 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 152–176 | 25 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 152–299 | 100 | 12 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 155–281 | 37 | 7 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 156–159 | 4 | 1 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 156–159 | 4 | 1 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 161–269 | 75 | 6 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 164–168 | 5 | 1 | Undefined position; Undefined team |
| `53` | `86` | Position_Unknown | Team_Unknown | 167–277 | 14 | 5 | Undefined position; Undefined team |
| `54` | `87` | Position_Unknown | Team_Unknown | 167–169 | 3 | 1 | Undefined position; Undefined team |
| `55` | `88` | Position_Unknown | Team_Unknown | 167–296 | 90 | 4 | Undefined position; Undefined team |
| `56` | `89` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `57` | `91` | Position_Unknown | Team_Unknown | 172–299 | 128 | 1 | Undefined position; Undefined team |
| `58` | `94` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `59` | `96` | Position_Unknown | Team_Unknown | 191–299 | 107 | 3 | Undefined position; Undefined team |
| `60` | `97` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |
| `61` | `99` | Position_Unknown | Team_Unknown | 196–278 | 42 | 6 | Undefined position; Undefined team |
| `62` | `100` | Position_Unknown | Team_Unknown | 202–299 | 7 | 3 | Undefined position; Undefined team |
| `63` | `101` | Position_Unknown | Team_Unknown | 202–211 | 6 | 2 | Undefined position; Undefined team |
| `64` | `102` | Position_Unknown | Team_Unknown | 216–299 | 84 | 1 | Undefined position; Undefined team |
| `65` | `106` | Position_Unknown | Team_Unknown | 233–281 | 46 | 3 | Undefined position; Undefined team |
| `66` | `107` | Position_Unknown | Team_Unknown | 234–292 | 56 | 2 | Undefined position; Undefined team |
| `67` | `108` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `68` | `110` | Position_Unknown | Team_Unknown | 240–272 | 14 | 5 | Undefined position; Undefined team |
| `69` | `111` | Position_Unknown | Team_Unknown | 241–278 | 18 | 3 | Undefined position; Undefined team |
| `70` | `113` | Position_Unknown | Team_Unknown | 241–251 | 7 | 2 | Undefined position; Undefined team |
| `71` | `114` | Position_Unknown | Team_Unknown | 245–299 | 45 | 6 | Undefined position; Undefined team |
| `72` | `121` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `73` | `122` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `74` | `125` | Position_Unknown | Team_Unknown | 262–299 | 27 | 2 | Undefined position; Undefined team |
| `75` | `129` | Position_Unknown | Team_Unknown | 264–284 | 8 | 3 | Undefined position; Undefined team |
| `76` | `130` | Position_Unknown | Team_Unknown | 264–275 | 12 | 1 | Undefined position; Undefined team |
| `77` | `133` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `78` | `135` | Position_Unknown | Team_Unknown | 265–275 | 10 | 2 | Undefined position; Undefined team |
| `79` | `141` | Position_Unknown | Team_Unknown | 266–299 | 12 | 3 | Undefined position; Undefined team |
| `80` | `145` | Position_Unknown | Team_Unknown | 268–294 | 12 | 4 | Undefined position; Undefined team |
| `81` | `146` | Position_Unknown | Team_Unknown | 269–283 | 12 | 3 | Undefined position; Undefined team |
| `82` | `150` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `83` | `152` | Position_Unknown | Team_Unknown | 272–276 | 4 | 2 | Undefined position; Undefined team |
| `84` | `162` | Position_Unknown | Team_Unknown | 275–296 | 9 | 4 | Undefined position; Undefined team |
| `85` | `166` | Position_Unknown | Team_Unknown | 281–283 | 3 | 1 | Undefined position; Undefined team |
| `86` | `170` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |
| `87` | `171` | Position_Unknown | Team_Unknown | 291–298 | 8 | 1 | Undefined position; Undefined team |
| `88` | `172` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `7` (Right_Gunner)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Guard` position mapped to `offense` team
- ⚠️ 69 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 69 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 138 |
| Missing visible bounding boxes during action | 260 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 4: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '7' has invalid range: start=233, end=45. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-167] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-202] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-42] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-134] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-86] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-282] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-94] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-129] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-51] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-100] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-172] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-278] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-111] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-212] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-284] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-62] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-254] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-51] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [48-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [82-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [126-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [1-46] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-132] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-106] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-133] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-74] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-133] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-104] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-105] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-253] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-136] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-170] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-202] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-152] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-212] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-258] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-176] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-211] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-252] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-277] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-169] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-203] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-252] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-296] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-211] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-257] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-281] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-285] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-288] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-283] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-275] for track '76' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '80' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '81' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>