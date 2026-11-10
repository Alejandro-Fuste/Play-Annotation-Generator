# Play-Annotation-Generator Annotation Review — RPO_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_77`
- **Frame Range:** 0 to 801 (802 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 801
- **Player Tracks:** 71
- **Ball Tracks:** 1
- **Action Segments:** 169
- **Validation Warnings:** 230
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `0` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 150
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_RunBlock` | C | `12` | `12` | 77 | START | 77 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `14` | `14` | 77 | START | 77 | 107 |
| ✅ EXACT | `Action_RunBlock` | LG | `16` | `16` | 77 | START | 77 | 120 |
| ✅ EXACT | `Action_RunBlock` | LT | `17` | `17` | 77 | START | 77 | 120 |
| ✅ EXACT | `Action_RunBlock` | RT | `18` | `18` | 77 | START | 77 | 120 |
| ✅ EXACT | `Action_ReadDefender` | QB | `20` | `20` | 78 | START | 78 | 80 |
| ✅ EXACT | `Action_PullBall` | QB | `20` | `20` | 81 | START | 81 | 89 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 114 | START | 114 | 120 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_PullBall` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 113 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 114 | 120 | 7 | inferred_complete_timeline |
| `Action_None` | 121 | 236 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 240 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 270 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 215 | 140 | inferred_complete_timeline |
| `Action_None` | 217 | 286 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 203 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 117 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 237 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 208 | 88 | inferred_complete_timeline |
| `Action_None` | 210 | 236 | 27 | inferred_complete_timeline |
| `Action_None` | 239 | 251 | 13 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 260 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 158 | 38 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 183 | 15 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 247 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 107 | 31 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 121 | 208 | 88 | inferred_complete_timeline |
| `Action_None` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 237 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 191 | 71 | inferred_complete_timeline |
| `Action_None` | 194 | 219 | 26 | inferred_complete_timeline |
| `Action_None` | 221 | 237 | 17 | inferred_complete_timeline |
| `Action_None` | 239 | 251 | 13 | inferred_complete_timeline |
| `Action_None` | 253 | 270 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 141 | 66 | inferred_complete_timeline |
| `Action_None` | 143 | 169 | 27 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 185 | 110 | inferred_complete_timeline |
| `Action_None` | 187 | 222 | 36 | inferred_complete_timeline |
| `Action_None` | 227 | 235 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 116 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 312 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 204 | 129 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 235 | 15 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 267 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 283 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 274 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 312 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 221 | 146 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 369 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 341 | 266 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 87–88 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 115–238 | 124 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 115–242 | 80 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 130–249 | 113 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 142–147 | 4 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 182–236 | 45 | 6 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 228–298 | 70 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 247–265 | 16 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 309–369 | 60 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 328–363 | 36 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 413–630 | 218 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 413–613 | 201 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 413–613 | 192 | 3 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 413–642 | 230 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 413–619 | 202 | 2 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 413–689 | 277 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 413–597 | 185 | 1 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 413–610 | 198 | 1 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 413–663 | 251 | 1 | Undefined position; Undefined team |
| `46` | `53` | Position_Unknown | Team_Unknown | 413–613 | 201 | 1 | Undefined position; Undefined team |
| `47` | `54` | Position_Unknown | Team_Unknown | 413–622 | 210 | 1 | Undefined position; Undefined team |
| `48` | `55` | Position_Unknown | Team_Unknown | 413–642 | 230 | 1 | Undefined position; Undefined team |
| `49` | `56` | Position_Unknown | Team_Unknown | 413–774 | 341 | 5 | Undefined position; Undefined team |
| `50` | `57` | Position_Unknown | Team_Unknown | 413–555 | 141 | 2 | Undefined position; Undefined team |
| `51` | `58` | Position_Unknown | Team_Unknown | 413–618 | 203 | 2 | Undefined position; Undefined team |
| `52` | `59` | Position_Unknown | Team_Unknown | 413–616 | 203 | 2 | Undefined position; Undefined team |
| `54` | `63` | Position_Unknown | Team_Unknown | 541–605 | 16 | 2 | Undefined position; Undefined team |
| `55` | `64` | Position_Unknown | Team_Unknown | 565–649 | 82 | 3 | Undefined position; Undefined team |
| `56` | `65` | Position_Unknown | Team_Unknown | 571–572 | 2 | 1 | Undefined position; Undefined team |
| `57` | `66` | Position_Unknown | Team_Unknown | 583–596 | 14 | 1 | Undefined position; Undefined team |
| `58` | `67` | Position_Unknown | Team_Unknown | 585–599 | 15 | 1 | Undefined position; Undefined team |
| `59` | `68` | Position_Unknown | Team_Unknown | 596–652 | 49 | 2 | Undefined position; Undefined team |
| `60` | `69` | Position_Unknown | Team_Unknown | 606–801 | 158 | 2 | Undefined position; Undefined team |
| `61` | `70` | Position_Unknown | Team_Unknown | 607–646 | 40 | 1 | Undefined position; Undefined team |
| `62` | `71` | Position_Unknown | Team_Unknown | 618–621 | 4 | 1 | Undefined position; Undefined team |
| `63` | `72` | Position_Unknown | Team_Unknown | 631–673 | 7 | 2 | Undefined position; Undefined team |
| `64` | `73` | Position_Unknown | Team_Unknown | 632–670 | 4 | 2 | Undefined position; Undefined team |
| `65` | `74` | Position_Unknown | Team_Unknown | 669–670 | 2 | 1 | Undefined position; Undefined team |
| `66` | `75` | Position_Unknown | Team_Unknown | 671–682 | 12 | 1 | Undefined position; Undefined team |
| `67` | `76` | Position_Unknown | Team_Unknown | 690–702 | 13 | 1 | Undefined position; Undefined team |
| `68` | `79` | Position_Unknown | Team_Unknown | 706–789 | 84 | 1 | Undefined position; Undefined team |
| `69` | `81` | Position_Unknown | Team_Unknown | 749–763 | 15 | 1 | Undefined position; Undefined team |
| `70` | `82` | Position_Unknown | Team_Unknown | 761–801 | 41 | 1 | Undefined position; Undefined team |
| `71` | `83` | Position_Unknown | Team_Unknown | 773–801 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `53` | `62` | 534 | 536 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 49 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 49 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 98 |
| Missing visible bounding boxes during action | 131 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 801 as fallback play end.
- ⚠️ Action 'Action_None' range [76-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-141] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-286] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-204] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-267] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-221] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-369] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-312] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-274] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-208] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-219] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-270] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-341] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-240] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-218] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-249] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-217] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-265] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-369] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-363] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-630] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-613] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-572] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-605] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-642] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-557] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-619] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-689] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-597] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-610] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-663] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-613] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-622] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-642] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-555] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-577] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-774] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-546] for track '50' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-555] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-540] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-618] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-598] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-616] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-543] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-605] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-583] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-649] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-596] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-599] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-599] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-652] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-751] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-646] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-621] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-633] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-673] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-670] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [671-682] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-702] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [706-789] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-763] for track '69' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.

</details>