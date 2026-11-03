# Play-Annotation-Generator Annotation Review — StopAndGo_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_45`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 175
- **Validation Warnings:** 193
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 16 | START | 16 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 19 | START | 30 | 34 |
| ✅ EXACT | `Action_PassBlock` | LT | `15` | `15` | 19 | START | 19 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 19 | START | 19 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 19 | START | 19 | 36 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 29 | END | 16 | 29 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `3` | `3` | 29 | START | 29 | 57 |
| ✅ EXACT | `Action_SellStop` | WR1 | `3` | `3` | 58 | START | 58 | 78 |
| ✅ EXACT | `Action_PumpFake` | QB | `8` | `8` | 64 | START | 64 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `3` | `3` | 79 | START | 79 | 118 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 103 | START | 103 | 116 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_None` | 30 | 63 | 34 | inferred_complete_timeline |
| `Action_PumpFake` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_None` | 78 | 102 | 25 | inferred_complete_timeline |
| `Action_ThrowPass` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 131 | 15 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 159 | 171 | 13 | inferred_complete_timeline |
| `Action_None` | 173 | 269 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 37 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_VerticalStem` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_SellStop` | 58 | 78 | 21 | inferred_complete_timeline |
| `Action_RunGoRoute` | 79 | 118 | 40 | inferred_complete_timeline |
| `Action_RunGoRoute` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_RunGoRoute` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 215 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 41 | 26 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 151 | 168 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 28 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 36 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 135 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 155 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 165 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 178 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 40 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 65 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_None` | 30 | 35 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 38 | 23 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 44 | 29 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_None` | 119 | 136 | 18 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 149 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 42 | 27 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 149 | 134 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 171 | 156 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 203 | 24 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 218 | 7 | inferred_complete_timeline |
| `Action_None` | 230 | 246 | 17 | inferred_complete_timeline |
| `Action_None` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 32 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 118 | 103 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 73 | 58 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 118 | 32 | inferred_complete_timeline |
| `Action_None` | 127 | 161 | 35 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 135 | 120 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 20–31 | 7 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 44–100 | 55 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–203 | 128 | 7 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 61–260 | 198 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 78–99 | 22 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 103–160 | 6 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 103–269 | 60 | 8 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 119–130 | 11 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 122–130 | 8 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 149–171 | 23 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 158–168 | 11 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 168–172 | 5 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 170–205 | 35 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 183–269 | 87 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 183–269 | 83 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 192–269 | 72 | 3 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 204–269 | 21 | 3 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 208–269 | 34 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 210–216 | 6 | 2 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 214–258 | 32 | 6 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 218–269 | 30 | 4 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 227–269 | 37 | 2 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 235–269 | 17 | 5 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 138 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [16–29], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=30.
- ⚠️ Action 'Action_None' range [16-135] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [79-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [123-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [133-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-37] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-171] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-203] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-149] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [16-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-135] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [138-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-155] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-168] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-40] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-59] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-136] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-186] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-209] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-260] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-189] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-205] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-238] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-255] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '45' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>