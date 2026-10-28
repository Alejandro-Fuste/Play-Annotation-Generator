# Play-Annotation-Generator Annotation Review — Draw_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_3`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 64 | START | 64 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `15` | 67 | START | 67 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `16` | 67 | START | 67 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `17` | 67 | START | 84 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `20` | 67 | START | 67 | 150 |
| ✅ EXACT | `Action_PassBlock` | LG | `22` | `21` | 67 | START | 67 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 83 | END | 64 | 83 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `19` | `18` | 87 | START | 87 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `19` | `18` | 100 | START | 100 | 166 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 166 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 185 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 108 | 45 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 237 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 252 | 12 | inferred_complete_timeline |
| `Action_None` | 254 | 257 | 4 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 175 | 112 | inferred_complete_timeline |
| `Action_None` | 178 | 265 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 262 | 199 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 269 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 269 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 150 | 84 | inferred_complete_timeline |
| `Action_None` | 151 | 269 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 110 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 103 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 150 | 84 | inferred_complete_timeline |
| `Action_None` | 151 | 167 | 17 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_None` | 197 | 216 | 20 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 233 | 240 | 8 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 150 | 84 | inferred_complete_timeline |
| `Action_None` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 205 | 142 | inferred_complete_timeline |
| `Action_None` | 211 | 269 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 97 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 97 | 34 | inferred_complete_timeline |
| `Action_None` | 100 | 159 | 60 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 252 | 43 | inferred_complete_timeline |
| `Action_None` | 254 | 262 | 9 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 110 | 47 | inferred_complete_timeline |
| `Action_None` | 115 | 136 | 22 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 166 | 103 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 197 | 230 | 34 | inferred_complete_timeline |
| `Action_None` | 232 | 269 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 167 | 104 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 178 | 185 | 8 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 212 | 16 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 229 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 237 | 5 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 269 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 231 | 168 | inferred_complete_timeline |
| `Action_None` | 233 | 237 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 159 | 96 | inferred_complete_timeline |
| `Action_None` | 161 | 269 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 221 | 158 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 232 | 243 | 12 | inferred_complete_timeline |
| `Action_None` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 200 | 137 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 231 | 18 | inferred_complete_timeline |
| `Action_None` | 234 | 269 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 124–164 | 41 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 132–269 | 110 | 10 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 132–269 | 129 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 191–269 | 76 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 193–263 | 52 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 198–266 | 25 | 6 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 233–236 | 4 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 237–252 | 14 | 3 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 255–260 | 4 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 257–269 | 9 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 118 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [64–83], lower_priority='Action_PassBlock' annotated_start=67, effective_Action_PassBlock_start=84.
- ⚠️ Action 'Action_None' range [64-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-265] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-269] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-243] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-205] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-269] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-166] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-230] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-269] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-231] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-167] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-212] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-252] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-110] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-97] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-216] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-240] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '17' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [84-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-103] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-166] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-185] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-252] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-163] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-169] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-216] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-230] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-263] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-252] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
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

</details>