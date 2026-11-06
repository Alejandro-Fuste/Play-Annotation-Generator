# Play-Annotation-Generator Annotation Review — PuntCoverage_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_23`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 183
- **Validation Warnings:** 213
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 165
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `38` | `30` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `38` | `30` |
| ❌ MISSING SEGMENT | `Action_Tackle` | Left_Gunner | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `6` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 18 | START | 18 | 47 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 45 | END | 45 | 45 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 68 | START | 68 | 84 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `38` | `30` | 190 | START | 190 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `38` | `30` | 230 | START | 230 | 245 |
| ❌ MISSING SEGMENT | `Action_Tackle` | Left_Gunner | `6` | `6` | 247 | START | N/A | N/A |

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
- **Visible Frames:** 0–129
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 70 | 53 | inferred_complete_timeline |
| `Action_None` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 122 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 152 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 246 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 92 | 75 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 18 | 47 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 52 | 60 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 77 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 80 | 63 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 104 | 87 | inferred_complete_timeline |
| `Action_None` | 106 | 142 | 37 | inferred_complete_timeline |
| `Action_None` | 149 | 329 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 67 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 68 | 84 | 17 | inferred_complete_timeline |
| `Action_None` | 85 | 135 | 51 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 41 | 24 | inferred_complete_timeline |
| `Action_None` | 44 | 62 | 19 | inferred_complete_timeline |
| `Action_None` | 67 | 70 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 94 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |
| `Action_None` | 57 | 208 | 152 | inferred_complete_timeline |
| `Action_None` | 212 | 228 | 17 | inferred_complete_timeline |
| `Action_None` | 230 | 310 | 81 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 55 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 208 | 191 | inferred_complete_timeline |
| `Action_None` | 213 | 228 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 99 | 82 | inferred_complete_timeline |
| `Action_None` | 104 | 112 | 9 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 147 | 130 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 203 | 18 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 109 | 92 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 118 | 5 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 284 | 99 | inferred_complete_timeline |
| `Action_None` | 286 | 329 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 329 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |
| `Action_None` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_None` | 125 | 167 | 43 | inferred_complete_timeline |
| `Action_None` | 178 | 186 | 9 | inferred_complete_timeline |
| `Action_None` | 197 | 216 | 20 | inferred_complete_timeline |
| `Action_None` | 219 | 234 | 16 | inferred_complete_timeline |
| `Action_None` | 237 | 244 | 8 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |
| `Action_None` | 260 | 305 | 46 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 182 | 165 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 196 | 238 | 43 | inferred_complete_timeline |
| `Action_None` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 302 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 154 | 137 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 275 | 85 | inferred_complete_timeline |
| `Action_None` | 280 | 284 | 5 | inferred_complete_timeline |
| `Action_None` | 286 | 329 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 89 | 72 | inferred_complete_timeline |
| `Action_None` | 91 | 164 | 74 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 176 | 302 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 45–82 | 29 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 63–129 | 18 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 67–303 | 237 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 71–76 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 81–96 | 16 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 86–259 | 152 | 14 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 94–329 | 227 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 96–171 | 75 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 97–289 | 183 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 104–329 | 226 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 124–272 | 131 | 8 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 146–302 | 145 | 6 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 156–307 | 130 | 5 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 172–329 | 158 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 186–302 | 110 | 3 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 203–205 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 210–244 | 34 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 222–329 | 102 | 3 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 245–302 | 58 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 268–302 | 35 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 269–302 | 34 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 274–292 | 19 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 303–329 | 23 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 303–307 | 5 | 1 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `38` (4 segments found)
- ❌ Missing segment for action `Action_Tackle` on target `6` (Left_Gunner)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 152 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_Tackle' for track '6' has invalid range: start=247, end=246. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-164] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-302] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-135] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-55] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-152] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-246] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-147] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-109] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-112] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-208] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-310] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-234] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-305] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-104] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-142] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-62] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-80] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [18-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [52-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-77] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-70] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-70] for track '20' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-303] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-96] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-113] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-137] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-259] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-171] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-168] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-222] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-289] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-134] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-184] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-286] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-264] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-273] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-307] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-277] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-292] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-244] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-302] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-302] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-302] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-292] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-321] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-329] for track '45' has 2 frames without a visible bounding box.
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

</details>