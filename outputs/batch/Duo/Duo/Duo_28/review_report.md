# Play-Annotation-Generator Annotation Review — Duo_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_28`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | TE2 | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | defense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 281 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | TE2 | `11` | `11` | 168 | START | 168 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `14` | `14` | 168 | START | 168 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `15` | `15` | 168 | START | 168 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `16` | `16` | 168 | START | 168 | 176 |
| ✅ EXACT | `Action_BlockSecondLevel` | DE2 | `10` | `10` | 185 | START | 185 | 188 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 281 | 282 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 287 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 177 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 328 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ComboBlock` | 168 | 196 | 29 | inferred_complete_timeline |
| `Action_ComboBlock` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 202 | 224 | 23 | inferred_complete_timeline |
| `Action_None` | 225 | 240 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ComboBlock` | 168 | 177 | 10 | inferred_complete_timeline |
| `Action_ComboBlock` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_ComboBlock` | 168 | 176 | 9 | inferred_complete_timeline |
| `Action_ComboBlock` | 179 | 188 | 10 | inferred_complete_timeline |
| `Action_ComboBlock` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_ComboBlock` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_ComboBlock` | 217 | 224 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 247 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 167 | 70 | inferred_complete_timeline |
| `Action_ComboBlock` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 173 | 197 | 25 | inferred_complete_timeline |
| `Action_ComboBlock` | 202 | 210 | 9 | inferred_complete_timeline |
| `Action_ComboBlock` | 224 | 224 | 1 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 185 | 188 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 305 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 321 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 208 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 297 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–77 | 11 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 183–328 | 145 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 188–228 | 37 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 209–225 | 17 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 210–328 | 116 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 236–328 | 92 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 245–328 | 84 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 245–254 | 10 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 254–281 | 27 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 270–273 | 4 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 271–272 | 2 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 328–328 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `16` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 62 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-321] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-177] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-290] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-281] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [185-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [168-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [199-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-219] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [168-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [173-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [202-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 225, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [225-230] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [168-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [179-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [184-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [168-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [179-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [201-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [208-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-232] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-228] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-254] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-276] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-273] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>