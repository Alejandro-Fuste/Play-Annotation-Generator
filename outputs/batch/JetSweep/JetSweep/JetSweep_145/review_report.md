# Play-Annotation-Generator Annotation Review — JetSweep_145

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_145`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 219
- **Validation Warnings:** 224
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 193
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR1 | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Toss` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 28 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR1 | `16` | `15` | 33 | START | 33 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `15` | `14` | 53 | START | 53 | 56 |
| ✅ EXACT | `Action_LeadBlock` | RB | `1` | `0` | 55 | START | 55 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 55 | START | 69 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 55 | START | 55 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 55 | START | 55 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 55 | START | 55 | 71 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `22` | `21` | 55 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 68 | END | 53 | 68 |
| ✅ EXACT | `Action_Toss` | QB | `3` | `2` | 73 | START | 73 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `16` | `15` | 84 | START | 84 | 136 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 68 | 16 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_Toss` | 73 | 83 | 11 | inferred_complete_timeline |
| `Action_None` | 84 | 269 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_LeadBlock` | 55 | 149 | 95 | inferred_complete_timeline |
| `Action_None` | 150 | 166 | 17 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_JetMotion` | 33 | 70 | 38 | inferred_complete_timeline |
| `Action_JetMotion` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 136 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 177 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 183 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 68 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 85 | 33 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 127 | 138 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_None` | 79 | 87 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 71 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 140 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 149 | 1 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_None` | 170 | 177 | 8 | inferred_complete_timeline |
| `Action_None` | 179 | 207 | 29 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 62 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 71 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_BallSnap` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 28–35
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 118 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 173 | 22 | inferred_complete_timeline |
| `Action_None` | 179 | 185 | 7 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 235 | 6 | inferred_complete_timeline |
| `Action_None` | 237 | 269 | 33 | inferred_complete_timeline |

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
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 115 | 41 | inferred_complete_timeline |
| `Action_None` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |
| `Action_None` | 152 | 158 | 7 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 196 | 31 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 227 | 19 | inferred_complete_timeline |
| `Action_None` | 231 | 269 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_None` | 66 | 72 | 7 | inferred_complete_timeline |
| `Action_None` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_None` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 70 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 98 | 46 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 98 | 46 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 269 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 136 | 84 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 106 | 54 | inferred_complete_timeline |
| `Action_None` | 109 | 117 | 9 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 138 | 7 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 158 | 9 | inferred_complete_timeline |
| `Action_None` | 160 | 200 | 41 | inferred_complete_timeline |
| `Action_None` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 181 | 129 | inferred_complete_timeline |
| `Action_None` | 192 | 196 | 5 | inferred_complete_timeline |
| `Action_None` | 210 | 224 | 15 | inferred_complete_timeline |
| `Action_None` | 232 | 245 | 14 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 69–122 | 44 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 80–269 | 128 | 9 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 83–185 | 74 | 6 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 106–269 | 155 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 107–269 | 154 | 5 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 128–269 | 121 | 8 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 130–269 | 132 | 4 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 140–269 | 111 | 7 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 150–158 | 9 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 161–218 | 51 | 5 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 181–269 | 46 | 5 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 199–269 | 50 | 6 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 208–269 | 61 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 212–269 | 49 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 213–269 | 45 | 4 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 240–246 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `41` | `53` | 263 | 265 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallSnap` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (10 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 179 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 291: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '0' (RB) duration 95 frames exceeds threshold 90 frames [start=55, end=149].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [53–68], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=69.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 95 frames exceeds threshold 90 frames [start=55, end=149].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 95 frames exceeds threshold 90 frames [start=55, end=149].
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=55, end=35. Clamping end to start.
- ⚠️ Action 'Action_None' range [150-166] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-98] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-136] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-200] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-245] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-196] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [53-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [59-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [33-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [79-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-158] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-177] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [128-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-147] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-98] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-118] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-158] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-188] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-225] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-158] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-202] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-224] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-246] for track '40' has 1 frames without a visible bounding box.
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

</details>