# Play-Annotation-Generator Annotation Review — StopAndGo_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_55`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 193
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 139
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR3 | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `17` | `17` | 18 | START | 18 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 21 | START | 21 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 21 | START | 21 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 21 | START | 37 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 21 | START | 21 | 41 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 36 | END | 18 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | `5` | `5` | 43 | START | 43 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR3 | `5` | `5` | 90 | START | 90 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `5` | `5` | 101 | START | 101 | 104 |
| ✅ EXACT | `Action_ThrowPass` | QB | `19` | `19` | 125 | START | 125 | 134 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 36 | 19 | inferred_complete_timeline |
| `Action_None` | 37 | 124 | 88 | inferred_complete_timeline |
| `Action_ThrowPass` | 125 | 134 | 10 | inferred_complete_timeline |
| `Action_None` | 135 | 191 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 212 | 195 | inferred_complete_timeline |
| `Action_None` | 215 | 329 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |
| `Action_None` | 183 | 196 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_VerticalStem` | 43 | 71 | 29 | inferred_complete_timeline |
| `Action_VerticalStem` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_VerticalStem` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_SellStop` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_SellStop` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_SellStop` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_RunGoRoute` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_RunGoRoute` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_RunGoRoute` | 110 | 168 | 59 | inferred_complete_timeline |
| `Action_RunGoRoute` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_RunGoRoute` | 177 | 202 | 26 | inferred_complete_timeline |
| `Action_RunGoRoute` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_RunGoRoute` | 220 | 223 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 55 | 38 | inferred_complete_timeline |
| `Action_None` | 58 | 143 | 86 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 41 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 77 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 138 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 191 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 215 | 229 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 235 | 315 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 28 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 92 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 153 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 67 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 150 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 290 | 135 | inferred_complete_timeline |
| `Action_PassBlock` | 295 | 329 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 133 | 116 | inferred_complete_timeline |
| `Action_None` | 148 | 153 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 67 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 106 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 46 | 29 | inferred_complete_timeline |
| `Action_None` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_None` | 83 | 112 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 108 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 120 | 103 | inferred_complete_timeline |
| `Action_None` | 123 | 237 | 115 | inferred_complete_timeline |
| `Action_None` | 239 | 329 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 73 | 56 | inferred_complete_timeline |
| `Action_None` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 329 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 147 | 130 | inferred_complete_timeline |
| `Action_None` | 153 | 173 | 21 | inferred_complete_timeline |
| `Action_None` | 183 | 206 | 24 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 329 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 203 | 186 | inferred_complete_timeline |
| `Action_None` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 241 | 14 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 26–57 | 32 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 31–135 | 80 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–150 | 97 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 63–272 | 209 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 121–285 | 143 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 140–215 | 75 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 147–183 | 22 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 151–329 | 179 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 158–329 | 169 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 158–220 | 31 | 5 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 212–329 | 114 | 3 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 232–234 | 3 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 235–240 | 6 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 243–260 | 11 | 2 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 251–253 | 3 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 255–257 | 3 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 281–329 | 41 | 4 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 302–304 | 3 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 306–326 | 18 | 2 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 310–311 | 2 | 1 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 312–329 | 15 | 2 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `50` | `75` | Position_Unknown | Team_Unknown | 313–329 | 16 | 2 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 317–329 | 12 | 2 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 321–329 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (9 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SellStop` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `5` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 124 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [18–36], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [18-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-241] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-147] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [43-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [78-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellStop' for track '5' starts at frame 90, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SellStop' range [90-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellStop' range [96-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [101-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [106-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [110-168] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [171-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [177-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [210-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [220-223] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-212] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-46] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [18-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [30-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '17' starts at frame 37, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [37-92] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [215-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [235-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-46] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-267] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-215] for track '26' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-183] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-234] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-178] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-287] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-329] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-292] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-315] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-325] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>