# Play-Annotation-Generator Annotation Review — Power_196

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_196`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 1
- **Action Segments:** 84
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | defense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 20 | START | 20 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 20 | START | 20 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 20 | START | 20 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 20 | START | 20 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 20 | START | 20 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 20 | START | 20 | 238 |
| ✅ EXACT | `Action_DownBlock` | LG | `10` | `10` | 182 | START | 182 | 254 |
| ✅ EXACT | `Action_DownBlock` | LT | `16` | `16` | 182 | START | 182 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | `9` | `9` | 182 | START | 182 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `17` | `17` | 182 | START | 182 | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–254
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 254 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 20–260
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 199 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 209 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 225 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 260 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 20–389
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 181 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 262 | 81 | inferred_complete_timeline |
| `Action_None` | 263 | 389 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 20–254
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 181 | 162 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 254 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 181 | 162 | inferred_complete_timeline |
| `Action_PullBlock` | 182 | 194 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 198 | 262 | 65 | inferred_complete_timeline |
| `Action_None` | 263 | 389 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–247
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 238 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 20–291
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 200 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 259 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 269 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 291 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 318 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 350 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 389 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 20–24
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 24 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–251
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 181 | 137 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 218 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 251 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–274
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 218 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 267 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 274 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–355
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 300 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 342 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 355 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–224
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 224 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 389 | 370 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 27–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 250 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 324 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 389 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 20–43 | 24 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 20–226 | 207 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 20–226 | 207 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 20–389 | 370 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 20–256 | 231 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 134–240 | 50 | 5 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 143–184 | 40 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 227–260 | 33 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 228–389 | 162 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 250–298 | 46 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 259–389 | 131 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 261–389 | 129 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 268–287 | 13 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 271–314 | 44 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 276–362 | 82 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 284–389 | 106 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 302–389 | 85 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 314–389 | 76 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 334–389 | 56 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 346–389 | 42 | 3 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 362–389 | 28 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 380–389 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | 146 | 163 | 9 | 50.0% | 152–158, 160–161 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 394: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-43] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-318] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-350] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-267] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-355] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-226] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [226-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-209] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-225] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-260] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-200] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-259] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-254] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-262] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-324] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-178] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-389] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-314] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-362] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-384] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-386] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>