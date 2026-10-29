# Play-Annotation-Generator Annotation Review — DeepCross_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_57`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 65
- **Ball Tracks:** 0
- **Action Segments:** 162
- **Validation Warnings:** 208
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 142
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 12 | START | 12 | 26 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 15 | START | 15 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 15 | START | 15 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 15 | START | 15 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 15 | START | 45 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 15 | START | 15 | 164 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `0` | `0` | 27 | START | 27 | 182 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 27 | END | 12 | 27 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 111 | START | 111 | 120 |

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
- **Visible Frames:** 0–263
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 27 | 16 | inferred_complete_timeline |
| `Action_None` | 28 | 110 | 83 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 120 | 10 | inferred_complete_timeline |
| `Action_None` | 121 | 174 | 54 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 160 | 149 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 209 | 41 | inferred_complete_timeline |
| `Action_None` | 212 | 232 | 21 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 247 | 236 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 27 | 182 | 156 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 244 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 106 | 95 | inferred_complete_timeline |
| `Action_None` | 110 | 170 | 61 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 242 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 83 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 176 | 162 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 189 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 203 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 224 | 238 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 26 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 135 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 162 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 208 | 216 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 224 | 243 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 164 | 150 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 178 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 177 | 163 | inferred_complete_timeline |
| `Action_PassBlock` | 199 | 202 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 179 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_None` | 69 | 159 | 91 | inferred_complete_timeline |
| `Action_None` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 88 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 179 | 48 | inferred_complete_timeline |
| `Action_None` | 185 | 241 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 135 | 124 | inferred_complete_timeline |
| `Action_None` | 137 | 216 | 80 | inferred_complete_timeline |
| `Action_None` | 218 | 240 | 23 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 221 | 210 | inferred_complete_timeline |
| `Action_None` | 223 | 235 | 13 | inferred_complete_timeline |
| `Action_None` | 237 | 243 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 247 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 206 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 178 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 255 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 72 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 52–235 | 146 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 94–246 | 113 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 105–110 | 6 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 128–245 | 47 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 171–173 | 3 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 185–248 | 39 | 6 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 188–202 | 11 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 202–244 | 37 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 206–246 | 39 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 213–243 | 11 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 225–250 | 11 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 225–232 | 8 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 226–245 | 20 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 228–251 | 17 | 4 | Undefined position; Undefined team |
| `36` | `108` | Position_Unknown | Team_Unknown | 267–318 | 52 | 1 | Undefined position; Undefined team |
| `37` | `109` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `38` | `111` | Position_Unknown | Team_Unknown | 281–287 | 7 | 1 | Undefined position; Undefined team |
| `39` | `113` | Position_Unknown | Team_Unknown | 284–311 | 20 | 2 | Undefined position; Undefined team |
| `40` | `114` | Position_Unknown | Team_Unknown | 284–319 | 36 | 1 | Undefined position; Undefined team |
| `41` | `115` | Position_Unknown | Team_Unknown | 284–389 | 70 | 2 | Undefined position; Undefined team |
| `42` | `116` | Position_Unknown | Team_Unknown | 284–318 | 34 | 2 | Undefined position; Undefined team |
| `43` | `117` | Position_Unknown | Team_Unknown | 284–389 | 67 | 3 | Undefined position; Undefined team |
| `44` | `118` | Position_Unknown | Team_Unknown | 284–318 | 33 | 2 | Undefined position; Undefined team |
| `45` | `119` | Position_Unknown | Team_Unknown | 286–319 | 34 | 1 | Undefined position; Undefined team |
| `46` | `120` | Position_Unknown | Team_Unknown | 286–318 | 33 | 1 | Undefined position; Undefined team |
| `47` | `123` | Position_Unknown | Team_Unknown | 291–305 | 14 | 2 | Undefined position; Undefined team |
| `48` | `125` | Position_Unknown | Team_Unknown | 313–389 | 38 | 3 | Undefined position; Undefined team |
| `49` | `140` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `50` | `141` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `51` | `142` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `52` | `143` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `53` | `144` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `54` | `145` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `55` | `146` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `56` | `147` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `57` | `148` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `58` | `149` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `59` | `150` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `60` | `151` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `61` | `152` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `62` | `153` | Position_Unknown | Team_Unknown | 357–389 | 33 | 1 | Undefined position; Undefined team |
| `63` | `154` | Position_Unknown | Team_Unknown | 359–389 | 31 | 1 | Undefined position; Undefined team |
| `64` | `155` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [12–27], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=28.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [27-182] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-209] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-159] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-179] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-170] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-242] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-244] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-177] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [199-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-189] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-203] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [210-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [214-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [224-238] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [12-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-135] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [208-216] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [220-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [224-243] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-164] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-216] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-235] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-179] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-232] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-318] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-300] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-319] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-319] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-318] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-318] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-318] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-319] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-318] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-300] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-389] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '64' has 1 frames without a visible bounding box.
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

</details>