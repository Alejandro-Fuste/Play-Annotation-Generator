# Play-Annotation-Generator Annotation Review — Duo_176

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_176`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 268
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `29` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `23` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `31` | `30` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 13 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 13 | START | 3 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `29` | `Group` | 13 | START | 9 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 13 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 13 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 13 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 13 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `9` | `Group` | 13 | START | 0 | 2 |
| ✅ EXACT | `Action_ComboBlock` | RG | `23` | `23` | 188 | START | 188 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `31` | `30` | 188 | START | 188 | 245 |
| ✅ EXACT | `Action_ComboBlock` | LT | `6` | `6` | 188 | START | 188 | 260 |
| ✅ EXACT | `Action_ComboBlock` | LG | `8` | `8` | 188 | START | 188 | 260 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 260 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `29`</summary>

- **xml_track_id:** `28`
- **actor_track_id:** `29`
- **team_side:** `offense`
- **Visible Frames:** 9–268
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 268 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 268 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 217 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 187 | 175 | inferred_complete_timeline |
| `Action_ComboBlock` | 188 | 260 | 73 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 187 | 175 | inferred_complete_timeline |
| `Action_ComboBlock` | 188 | 260 | 73 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 3–268
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 187 | 185 | inferred_complete_timeline |
| `Action_ComboBlock` | 188 | 260 | 73 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 244 | 232 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 196 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 268 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 241 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 190 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 196 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 189 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 232 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 250 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 268 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 268 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 51 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 209 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 268 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 3–12 | 10 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 3–13 | 10 | 2 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 3–13 | 11 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 10–13 | 4 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 14–268 | 150 | 9 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 133–139 | 7 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 143–268 | 123 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 194–268 | 75 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 219–268 | 50 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 224–235 | 8 | 3 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 231–268 | 31 | 3 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 254–268 | 15 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 262–268 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `31` (2 segments found)

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-250] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-268] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-244] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-232] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-268] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-268] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-189] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-12] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-13] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-61] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-136] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [188-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [247-260] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-268] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-256] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
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