# Play-Annotation-Generator Annotation Review — DeepCross_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_37`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 75
- **Ball Tracks:** 0
- **Action Segments:** 196
- **Validation Warnings:** 284
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 167
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `12` | 10 | START | 10 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 10 | START | 10 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 10 | START | 10 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 10 | START | 10 | 32 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 12 | END | 12 | 12 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `1` | `1` | 15 | START | 15 | 190 |
| ⚠️ START CHANGED | `Action_ThrowPass` | QB | `15` | `15` | 104 | START | 114 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `1` | `1` | 191 | START | 191 | 195 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 12 | 1 | inferred_complete_timeline |
| `Action_None` | 13 | 92 | 80 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 114 | 114 | 1 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 195 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 217 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 15 | 190 | 176 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 195 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 240 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 251 | 269 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 288 | 291 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 82 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 90 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 32 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 83 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 98 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 116 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 38 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 52 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 82 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 92 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 57 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 154 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 185 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 195 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 284 | 285 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 68 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 206 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 212 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 251 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–117 | 105 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–30 | 29 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 67–180 | 42 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 70–82 | 11 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 76–90 | 8 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 88–90 | 3 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 114–261 | 146 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 114–299 | 167 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 121–126 | 6 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 126–128 | 3 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 135–147 | 12 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 137–175 | 34 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 141–191 | 43 | 5 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 153–179 | 27 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 154–200 | 21 | 3 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 160–182 | 23 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 165–203 | 36 | 3 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 168–195 | 22 | 2 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 179–207 | 21 | 4 | Undefined position; Undefined team |
| `44` | `70` | Position_Unknown | Team_Unknown | 179–299 | 80 | 7 | Undefined position; Undefined team |
| `45` | `72` | Position_Unknown | Team_Unknown | 181–202 | 19 | 3 | Undefined position; Undefined team |
| `46` | `75` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `49` | `84` | Position_Unknown | Team_Unknown | 196–224 | 20 | 5 | Undefined position; Undefined team |
| `50` | `85` | Position_Unknown | Team_Unknown | 196–200 | 5 | 1 | Undefined position; Undefined team |
| `51` | `86` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `52` | `93` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `53` | `94` | Position_Unknown | Team_Unknown | 214–265 | 29 | 6 | Undefined position; Undefined team |
| `54` | `95` | Position_Unknown | Team_Unknown | 217–299 | 79 | 2 | Undefined position; Undefined team |
| `55` | `104` | Position_Unknown | Team_Unknown | 229–299 | 57 | 6 | Undefined position; Undefined team |
| `56` | `108` | Position_Unknown | Team_Unknown | 232–264 | 33 | 1 | Undefined position; Undefined team |
| `57` | `109` | Position_Unknown | Team_Unknown | 235–299 | 60 | 4 | Undefined position; Undefined team |
| `58` | `110` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `59` | `111` | Position_Unknown | Team_Unknown | 237–240 | 4 | 1 | Undefined position; Undefined team |
| `60` | `113` | Position_Unknown | Team_Unknown | 240–299 | 52 | 3 | Undefined position; Undefined team |
| `61` | `114` | Position_Unknown | Team_Unknown | 240–299 | 56 | 2 | Undefined position; Undefined team |
| `62` | `115` | Position_Unknown | Team_Unknown | 250–299 | 18 | 4 | Undefined position; Undefined team |
| `63` | `116` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `64` | `117` | Position_Unknown | Team_Unknown | 263–271 | 9 | 1 | Undefined position; Undefined team |
| `65` | `119` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `66` | `120` | Position_Unknown | Team_Unknown | 268–299 | 13 | 4 | Undefined position; Undefined team |
| `67` | `125` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `68` | `126` | Position_Unknown | Team_Unknown | 279–299 | 19 | 2 | Undefined position; Undefined team |
| `69` | `127` | Position_Unknown | Team_Unknown | 280–283 | 4 | 1 | Undefined position; Undefined team |
| `70` | `128` | Position_Unknown | Team_Unknown | 283–299 | 17 | 1 | Undefined position; Undefined team |
| `71` | `129` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |
| `72` | `130` | Position_Unknown | Team_Unknown | 292–299 | 6 | 2 | Undefined position; Undefined team |
| `73` | `131` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `74` | `132` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `15` (QB): Annotated start 104 != Inferred start 114
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 54 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 54 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 108 |
| Missing visible bounding boxes during action | 172 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 39: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 40: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-240] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-92] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-68] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-185] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-195] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-82] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-32] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-172] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-82] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-90] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-251] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-261] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-184] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-299] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-126] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-148] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-175] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-147] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-157] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-179] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-179] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-188] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-182] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-189] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-203] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-185] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-184] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-192] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-207] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-228] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-244] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-299] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-188] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-195] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-202] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-201] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-224] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-200] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-197] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-233] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-248] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-258] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-292] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-240] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-273] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-281] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-264] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-249] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-258] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-289] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-250] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-299] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-290] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-299] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-271] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-282] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-291] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-292] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-299] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>