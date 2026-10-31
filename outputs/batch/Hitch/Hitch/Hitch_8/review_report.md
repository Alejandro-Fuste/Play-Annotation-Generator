# Play-Annotation-Generator Annotation Review — Hitch_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_8`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 180
- **Validation Warnings:** 186
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 162
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR3 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 10 | START | 10 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 14 | START | 14 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 14 | START | 14 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 14 | START | 27 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 14 | START | 14 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR3 | `6` | `6` | 26 | START | 26 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 26 | END | 10 | 26 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 87 | START | 87 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `6` | `6` | 122 | START | 122 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 26 | 17 | inferred_complete_timeline |
| `Action_None` | 27 | 86 | 60 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 105 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 153 | 144 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 183 | 247 | 65 | inferred_complete_timeline |
| `Action_None` | 251 | 257 | 7 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 112 | 103 | inferred_complete_timeline |
| `Action_None` | 117 | 122 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 131 | 6 | inferred_complete_timeline |
| `Action_None` | 140 | 192 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 251 | 242 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 26 | 104 | 79 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 129 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 146 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 181 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 44 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 62 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 26 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 89 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 44 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 73 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 189 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 269 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 44 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 108 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 135 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 174 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 208 | 222 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 226 | 247 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 44 | 35 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_None` | 54 | 105 | 52 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 189 | 44 | inferred_complete_timeline |
| `Action_None` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 31 | 22 | inferred_complete_timeline |
| `Action_None` | 34 | 44 | 11 | inferred_complete_timeline |
| `Action_None` | 49 | 127 | 79 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 171 | 29 | inferred_complete_timeline |
| `Action_None` | 192 | 208 | 17 | inferred_complete_timeline |
| `Action_None` | 221 | 227 | 7 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 44 | 35 | inferred_complete_timeline |
| `Action_None` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 82 | 11 | inferred_complete_timeline |
| `Action_None` | 86 | 103 | 18 | inferred_complete_timeline |
| `Action_None` | 114 | 130 | 17 | inferred_complete_timeline |
| `Action_None` | 139 | 162 | 24 | inferred_complete_timeline |
| `Action_None` | 167 | 197 | 31 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 126 | 117 | inferred_complete_timeline |
| `Action_None` | 133 | 189 | 57 | inferred_complete_timeline |
| `Action_None` | 205 | 229 | 25 | inferred_complete_timeline |
| `Action_None` | 237 | 269 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 202 | 193 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 34 | 25 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 39 | 140 | 102 | inferred_complete_timeline |
| `Action_None` | 142 | 183 | 42 | inferred_complete_timeline |
| `Action_None` | 186 | 203 | 18 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 196 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 44 | 35 | inferred_complete_timeline |
| `Action_None` | 49 | 104 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 269 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 269 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 141 | 132 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–203 | 187 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 20–44 | 25 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 51–129 | 14 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 51–105 | 54 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 71–122 | 27 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 137–269 | 130 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 151–269 | 105 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 160–264 | 44 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 171–269 | 43 | 8 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 180–269 | 75 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 190–269 | 75 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 204–212 | 4 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 213–269 | 55 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 220–269 | 41 | 5 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 224–269 | 17 | 3 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 225–255 | 18 | 5 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 236–241 | 6 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 262–269 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (14 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunHitchRoute` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 141 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 14: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [10–26], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=27.
- ⚠️ Action 'Action_None' range [10-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-202] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-126] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-189] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-229] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [26-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [111-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [114-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [179-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-104] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-140] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-183] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-127] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-208] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-153] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-247] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-82] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-130] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-189] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-135] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [140-144] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-191] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [196-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [203-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [208-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [226-247] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [250-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [10-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-44] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-44] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-56] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-264] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-266] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-244] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-259] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>