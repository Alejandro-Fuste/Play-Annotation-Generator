# Play-Annotation-Generator Annotation Review — RPO_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_16`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `5` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 149
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 76 | START | 76 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `15` | 76 | START | 76 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 76 | START | 76 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 76 | START | 76 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 76 | START | 76 | 78 |
| ✅ EXACT | `Action_ReadDefender` | QB | `18` | `18` | 78 | START | 78 | 86 |
| ✅ EXACT | `Action_PullBall` | QB | `18` | `18` | 87 | START | 87 | 97 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 121 | START | 121 | 131 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 77 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 120 | 23 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 222 | 91 | inferred_complete_timeline |
| `Action_None` | 225 | 240 | 16 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 359 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 217 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 359 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 170 | 96 | inferred_complete_timeline |
| `Action_None` | 172 | 212 | 41 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 243 | 5 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 265 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 359 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 102 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 146 | 11 | inferred_complete_timeline |
| `Action_None` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 170 | 188 | 19 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 78 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 129 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 131 | 56 | inferred_complete_timeline |
| `Action_None` | 132 | 147 | 16 | inferred_complete_timeline |
| `Action_None` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 177 | 184 | 8 | inferred_complete_timeline |
| `Action_None` | 208 | 218 | 11 | inferred_complete_timeline |
| `Action_None` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 131 | 56 | inferred_complete_timeline |
| `Action_None` | 132 | 166 | 35 | inferred_complete_timeline |
| `Action_None` | 168 | 260 | 93 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 292 | 321 | 30 | inferred_complete_timeline |
| `Action_None` | 323 | 359 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 113 | 39 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 246 | 307 | 62 | inferred_complete_timeline |
| `Action_None` | 312 | 359 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 109 | 35 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 175 | 24 | inferred_complete_timeline |
| `Action_None` | 177 | 359 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 113 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 221 | 147 | inferred_complete_timeline |
| `Action_None` | 223 | 290 | 68 | inferred_complete_timeline |
| `Action_None` | 294 | 334 | 41 | inferred_complete_timeline |
| `Action_None` | 337 | 343 | 7 | inferred_complete_timeline |
| `Action_None` | 348 | 352 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 171 | 97 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 198 | 22 | inferred_complete_timeline |
| `Action_None` | 202 | 220 | 19 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 211 | 137 | inferred_complete_timeline |
| `Action_None` | 214 | 302 | 89 | inferred_complete_timeline |
| `Action_None` | 312 | 317 | 6 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 359 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–345
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 220 | 146 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_None` | 246 | 252 | 7 | inferred_complete_timeline |
| `Action_None` | 254 | 275 | 22 | inferred_complete_timeline |
| `Action_None` | 282 | 292 | 11 | inferred_complete_timeline |
| `Action_None` | 336 | 345 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 207 | 133 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 120 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 237 | 163 | inferred_complete_timeline |
| `Action_None` | 239 | 253 | 15 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 118–123 | 5 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 126–130 | 5 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 126–166 | 29 | 6 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 130–359 | 219 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 155–359 | 147 | 9 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 180–359 | 140 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 218–359 | 140 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 230–251 | 15 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 238–296 | 51 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 248–359 | 92 | 5 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 265–292 | 10 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 270–359 | 85 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 279–327 | 49 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 331–341 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 126 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [75-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-146] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-237] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-275] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-345] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-171] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-198] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-221] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-290] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-334] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-113] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-129] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-211] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-147] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-359] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-131] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-166] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-321] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-222] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-102] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-217] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-359] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-247] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-359] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-343] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-304] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-330] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-327] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-341] for track '35' has 2 frames without a visible bounding box.
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

</details>