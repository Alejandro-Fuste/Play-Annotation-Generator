# Play-Annotation-Generator Annotation Review — Draw_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_39`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 167
- **Validation Warnings:** 176
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 137
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 41 | START | 41 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `14` | 44 | START | 59 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `15` | 44 | START | 44 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `16` | 44 | START | 44 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `19` | 44 | START | 44 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 44 | START | 44 | 67 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 58 | END | 41 | 58 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `4` | `3` | 61 | START | 61 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `4` | `3` | 70 | START | 70 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 82 | START | 82 | 100 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 114 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 58 | 18 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 61 | 69 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 160 | 79 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 100 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 108 | 120 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 177 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 207 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 209 | 225 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 256 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 126 | 86 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 115 | 75 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 144 | 20 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 110 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 131 | 91 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 81 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 151 | 17 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 171 | 9 | inferred_complete_timeline |
| `Action_None` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 192 | 9 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 224 | 20 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 269 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 96 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 58 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 69 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 92 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 82 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 96 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 101 | 61 | inferred_complete_timeline |
| `Action_None` | 105 | 120 | 16 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 135 | 200 | 66 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 75 | 35 | inferred_complete_timeline |
| `Action_None` | 80 | 106 | 27 | inferred_complete_timeline |
| `Action_None` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 148 | 14 | inferred_complete_timeline |
| `Action_None` | 151 | 269 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 93 | 53 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 90 | 50 | inferred_complete_timeline |
| `Action_None` | 92 | 120 | 29 | inferred_complete_timeline |
| `Action_None` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 150 | 168 | 19 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 231 | 191 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 131 | 91 | inferred_complete_timeline |
| `Action_None` | 137 | 151 | 15 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 74 | 34 | inferred_complete_timeline |
| `Action_None` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_None` | 93 | 116 | 24 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 131 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 269 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 269 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 243 | 203 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 244 | 204 | inferred_complete_timeline |
| `Action_None` | 252 | 255 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 231 | 191 | inferred_complete_timeline |
| `Action_None` | 235 | 251 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–32 | 33 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 85–176 | 91 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 115–269 | 139 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 126–181 | 6 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 136–144 | 9 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 137–269 | 129 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 141–269 | 95 | 12 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 144–269 | 93 | 9 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 155–165 | 11 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 161–163 | 3 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 167–269 | 102 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 168–236 | 69 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 176–219 | 42 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 188–269 | 81 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 188–269 | 79 | 3 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 191–269 | 79 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 192–269 | 78 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 259–261 | 3 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (8 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [41–58], lower_priority='Action_PassBlock' annotated_start=44, effective_Action_PassBlock_start=59.
- ⚠️ Action 'Action_None' range [41-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-144] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-106] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-124] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [70-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [76-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-269] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-110] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-93] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-177] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-207] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-225] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-256] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-243] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-131] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-126] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-231] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-69] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-151] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-224] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-269] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-148] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-244] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-251] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-67] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-173] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-195] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-251] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-157] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-182] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-202] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-230] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-236] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '42' has 1 frames without a visible bounding box.
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

</details>