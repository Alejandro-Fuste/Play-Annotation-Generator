# Play-Annotation-Generator Annotation Review — InsideZoneRead_315

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_315`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 219
- **Validation Warnings:** 239
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 193
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Keep` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 14 | START | 14 | 27 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 17 | START | 17 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 17 | START | 17 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `17` | 17 | START | 17 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 17 | START | 28 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `19` | 17 | START | 17 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 27 | END | 14 | 27 |
| ✅ EXACT | `Action_ReadDefender` | QB | `22` | `21` | 32 | START | 32 | 38 |
| ✅ EXACT | `Action_Keep` | QB | `22` | `21` | 39 | START | 39 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `22` | `21` | 62 | START | 62 | 84 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_Keep` | 39 | 61 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 62 | 84 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 163 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 130 | 117 | inferred_complete_timeline |
| `Action_None` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 199 | 63 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 86 | 176 | 91 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 214 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 112 | 99 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 147 | 31 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 162 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 176 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 188 | 175 | inferred_complete_timeline |
| `Action_None` | 193 | 197 | 5 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 80 | 64 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 139 | 15 | inferred_complete_timeline |
| `Action_None` | 142 | 176 | 35 | inferred_complete_timeline |
| `Action_None` | 178 | 222 | 45 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 84 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 84 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_None` | 112 | 162 | 51 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 73 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 161 | 9 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 214 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 96 | 80 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 127 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 209 | 64 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 144 | 27 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 77 | 64 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 75 | 62 | inferred_complete_timeline |
| `Action_None` | 101 | 153 | 53 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 173 | 10 | inferred_complete_timeline |
| `Action_None` | 177 | 190 | 14 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 231 | 35 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 130 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 89 | 76 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 84 | 71 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 143 | 52 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 162 | 12 | inferred_complete_timeline |
| `Action_None` | 166 | 193 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 169 | 156 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 184 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 216 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 133 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 179 | 166 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 66–133 | 55 | 7 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 95–239 | 113 | 8 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 121–239 | 63 | 7 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 142–239 | 97 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 166–239 | 69 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 168–239 | 49 | 10 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 177–225 | 31 | 6 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 179–239 | 59 | 2 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `33` | `57` | Position_Unknown | Team_Unknown | 190–192 | 3 | 1 | Undefined position; Undefined team |
| `34` | `58` | Position_Unknown | Team_Unknown | 190–205 | 12 | 3 | Undefined position; Undefined team |
| `35` | `59` | Position_Unknown | Team_Unknown | 190–221 | 15 | 3 | Undefined position; Undefined team |
| `36` | `62` | Position_Unknown | Team_Unknown | 197–218 | 22 | 1 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 197–202 | 6 | 1 | Undefined position; Undefined team |
| `38` | `64` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 212–236 | 7 | 2 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `44` | `76` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `45` | `79` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `46` | `80` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `47` | `82` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `48` | `84` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `49` | `85` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `50` | `86` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (6 segments found)

### Track Identity Issues

- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 179 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [14–27], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=28.
- ⚠️ Action 'Action_None' range [14-112] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-147] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-130] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-199] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-214] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-144] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-153] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-190] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-231] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-162] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-193] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-43] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-222] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-169] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-184] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-179] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-77] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-84] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-133] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-84] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-91] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-162] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-127] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [39-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [62-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-133] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-163] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-239] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-87] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-113] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-163] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-236] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-187] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-219] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-218] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '50' has 1 frames without a visible bounding box.
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

</details>