# Play-Annotation-Generator Annotation Review — RPO_221

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_221`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 171
- **Validation Warnings:** 189
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 152
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `14` | 60 | START | 60 | 66 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 60 | START | 60 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `19` | 60 | START | 60 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 60 | START | 60 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 60 | START | 60 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `6` | `6` | 67 | START | 67 | 320 |
| ✅ EXACT | `Action_PullBall` | RB | `8` | `8` | 70 | START | 70 | 86 |
| ✅ EXACT | `Action_ThrowPass` | RB | `8` | `8` | 117 | START | 117 | 126 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 67 | 320 | 254 | inferred_complete_timeline |
| `Action_ReadDefender` | 323 | 329 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_PullBall` | 70 | 86 | 17 | inferred_complete_timeline |
| `Action_None` | 87 | 116 | 30 | inferred_complete_timeline |
| `Action_ThrowPass` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 167 | 109 | inferred_complete_timeline |
| `Action_None` | 177 | 221 | 45 | inferred_complete_timeline |
| `Action_None` | 226 | 249 | 24 | inferred_complete_timeline |
| `Action_None` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 303 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 181 | 123 | inferred_complete_timeline |
| `Action_None` | 195 | 304 | 110 | inferred_complete_timeline |
| `Action_None` | 306 | 316 | 11 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 329 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 126 | 67 | inferred_complete_timeline |
| `Action_None` | 127 | 138 | 12 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 329 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 60 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 96 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 126 | 67 | inferred_complete_timeline |
| `Action_None` | 127 | 203 | 77 | inferred_complete_timeline |
| `Action_None` | 208 | 329 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 126 | 46 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 134 | 214 | 81 | inferred_complete_timeline |
| `Action_None` | 216 | 313 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 82 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 92 | 34 | inferred_complete_timeline |
| `Action_None` | 94 | 329 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 329 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 131 | 73 | inferred_complete_timeline |
| `Action_None` | 138 | 151 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 297 | 239 | inferred_complete_timeline |
| `Action_None` | 300 | 329 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 329 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 228 | 170 | inferred_complete_timeline |
| `Action_None` | 231 | 252 | 22 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 142 | 84 | inferred_complete_timeline |
| `Action_None` | 153 | 177 | 25 | inferred_complete_timeline |
| `Action_None` | 181 | 197 | 17 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 307 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 197 | 139 | inferred_complete_timeline |
| `Action_None` | 199 | 208 | 10 | inferred_complete_timeline |
| `Action_None` | 210 | 216 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 191 | 133 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_None` | 224 | 235 | 12 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 306 | 61 | inferred_complete_timeline |
| `Action_None` | 308 | 329 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 194 | 136 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |
| `Action_None` | 212 | 216 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 61–329 | 259 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 80–87 | 8 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 85–111 | 11 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 89–97 | 9 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 100–108 | 5 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 105–113 | 8 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 130–329 | 196 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 144–169 | 26 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 153–329 | 176 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 163–176 | 14 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 172–178 | 7 | 1 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `36` | `59` | Position_Unknown | Team_Unknown | 176–263 | 28 | 9 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 190–329 | 140 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 199–329 | 88 | 10 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 213–324 | 101 | 6 | Undefined position; Undefined team |
| `40` | `66` | Position_Unknown | Team_Unknown | 222–245 | 11 | 3 | Undefined position; Undefined team |
| `41` | `67` | Position_Unknown | Team_Unknown | 225–274 | 6 | 3 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 254–314 | 55 | 2 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 266–310 | 29 | 4 | Undefined position; Undefined team |
| `46` | `82` | Position_Unknown | Team_Unknown | 280–309 | 16 | 3 | Undefined position; Undefined team |
| `47` | `84` | Position_Unknown | Team_Unknown | 286–292 | 7 | 1 | Undefined position; Undefined team |
| `48` | `90` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `49` | `92` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `50` | `93` | Position_Unknown | Team_Unknown | 309–329 | 21 | 1 | Undefined position; Undefined team |
| `51` | `94` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |
| `52` | `95` | Position_Unknown | Team_Unknown | 313–329 | 17 | 1 | Undefined position; Undefined team |
| `53` | `97` | Position_Unknown | Team_Unknown | 320–323 | 4 | 1 | Undefined position; Undefined team |
| `54` | `98` | Position_Unknown | Team_Unknown | 322–329 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 122 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [59-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-249] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-306] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [67-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [323-329] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-177] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-131] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-307] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-297] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '20' starts at frame 60, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [60-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-78] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-313] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-97] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-169] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-206] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-176] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-301] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-316] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-302] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-291] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '54' has 1 frames without a visible bounding box.
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

</details>