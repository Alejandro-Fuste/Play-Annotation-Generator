# Play-Annotation-Generator Annotation Review — Draw_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 2
- **Action Segments:** 152
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 131
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `9` | `8` | 41 | START | 41 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `16` | 44 | START | 44 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 44 | START | 44 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `18` | 44 | START | 44 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 44 | START | 44 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `20` | 44 | START | 44 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 47 | END | 41 | 47 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `22` | `21` | 53 | START | 53 | 84 |
| ✅ EXACT | `Action_BallCarry` | QB | `22` | `21` | 85 | START | 85 | 94 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 53 | 84 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 94 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 94 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 155 | 115 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 178 | 13 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 207 | 167 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 92 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 94 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 125 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 133 | 7 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 152 | 15 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 182 | 20 | inferred_complete_timeline |
| `Action_None` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 64 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 94 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 110 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 119 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 133 | 90 | inferred_complete_timeline |
| `Action_None` | 134 | 177 | 44 | inferred_complete_timeline |
| `Action_None` | 184 | 197 | 14 | inferred_complete_timeline |
| `Action_None` | 215 | 221 | 7 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 77 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 118 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 81 | 41 | inferred_complete_timeline |
| `Action_None` | 84 | 94 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 94 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 121 | 23 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 183 | 53 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 48 | 75 | 28 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 94 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_None` | 128 | 151 | 24 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 88 | 48 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 147 | 49 | inferred_complete_timeline |
| `Action_None` | 154 | 169 | 16 | inferred_complete_timeline |
| `Action_None` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_None` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 135 | 95 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 239 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 121 | 81 | inferred_complete_timeline |
| `Action_None` | 131 | 139 | 9 | inferred_complete_timeline |
| `Action_None` | 141 | 149 | 9 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 140 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 220 | 180 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 168 | 128 | inferred_complete_timeline |
| `Action_None` | 176 | 186 | 11 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 203 | 163 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 228 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 102 | 62 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–239 | 239 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 66–68 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 87–89 | 3 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 105–215 | 105 | 4 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 113–226 | 96 | 4 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 114–215 | 88 | 5 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 118–239 | 111 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 128–239 | 112 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 142–149 | 7 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 175–239 | 41 | 3 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 198–239 | 41 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 200–239 | 35 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `25` | 79 | 93 | 7 | 46.7% | 81–85, 87–89 |
| `30` | `42` | 140 | 141 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 24: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [41-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-155] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-232] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-220] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-75] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-151] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-228] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-147] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-121] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-183] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-94] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-118] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-125] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-182] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-177] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-94] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-118] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-132] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-170] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-215] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-203] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-139] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>