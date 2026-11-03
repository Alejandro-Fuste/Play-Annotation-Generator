# Play-Annotation-Generator Annotation Review — StopAndGo_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_29`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 26 | START | 26 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 29 | START | 29 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `2` | `2` | 29 | START | 29 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 29 | START | 29 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 29 | START | 37 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `9` | `9` | 29 | START | 29 | 94 |
| ✅ EXACT | `Action_SnapReceive` | WR1 | `1` | `1` | 36 | END | 26 | 36 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 36 | START | 36 | 90 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 91 | START | 91 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `0` | `0` | 108 | START | 108 | 140 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 138 | START | 138 | 148 |

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
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_ThrowPass` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_None` | 149 | 204 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 226 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 36 | 11 | inferred_complete_timeline |
| `Action_None` | 37 | 88 | 52 | inferred_complete_timeline |
| `Action_None` | 93 | 242 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 178 | 153 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_VerticalStem` | 36 | 90 | 55 | inferred_complete_timeline |
| `Action_SellStop` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 108 | 140 | 33 | inferred_complete_timeline |
| `Action_RunGoRoute` | 153 | 213 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 236 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 44 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 79 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 111 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 130 | 177 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 216 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 169 | 141 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 229 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 36 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 94 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 153 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 176 | 148 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 224 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 45 | 20 | inferred_complete_timeline |
| `Action_None` | 47 | 81 | 35 | inferred_complete_timeline |
| `Action_None` | 86 | 204 | 119 | inferred_complete_timeline |
| `Action_None` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 221 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 65 | 40 | inferred_complete_timeline |
| `Action_None` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_None` | 87 | 162 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 63 | 38 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 76 | 51 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 125 | 8 | inferred_complete_timeline |
| `Action_None` | 129 | 161 | 33 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 209 | 36 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 185 | 160 | inferred_complete_timeline |
| `Action_None` | 191 | 269 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 77 | 52 | inferred_complete_timeline |
| `Action_None` | 81 | 269 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 190 | 165 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 76 | 51 | inferred_complete_timeline |
| `Action_None` | 87 | 223 | 137 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 263 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 195 | 203 | 9 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 200 | 175 | inferred_complete_timeline |
| `Action_None` | 203 | 228 | 26 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 64–67 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 79–246 | 168 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 177–200 | 17 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 198–230 | 33 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 215–221 | 6 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 229–231 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 254–269 | 16 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [26–36], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_RunGoRoute' range [108-140] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [153-213] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-242] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-185] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-269] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-65] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-204] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-223] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-94] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-145] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-153] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-190] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-192] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-111] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [130-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [187-216] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [223-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-90] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-209] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-229] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-246] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '30' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>