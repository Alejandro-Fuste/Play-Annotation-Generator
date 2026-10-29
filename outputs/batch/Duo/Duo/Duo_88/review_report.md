# Play-Annotation-Generator Annotation Review — Duo_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_88`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 298
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | TE | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | SAF1 | defense | `14` | `14` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `25` | `23` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 298 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `9` | `Group` | 0 | START | 0 | 229 |
| ✅ EXACT | `Action_ComboBlock` | TE | `12` | `12` | 185 | START | 185 | 229 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | SAF1 | `14` | `14` | 185 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | QB | `18` | `18` | 185 | START | 185 | 229 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `20` | `20` | 185 | START | 185 | 229 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `25` | `23` | 199 | START | 199 | 229 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 229 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_ComboBlock` | 185 | 229 | 45 | inferred_complete_timeline |
| `Action_None` | 230 | 263 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 294 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 267 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 298 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 116 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 146 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 184 | 29 | inferred_complete_timeline |
| `Action_ComboBlock` | 185 | 229 | 45 | inferred_complete_timeline |
| `Action_None` | 230 | 279 | 50 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 145 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 288 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 250 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 275 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 172 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 268 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 160 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 257 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–298 | 286 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 67–101 | 15 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 77–291 | 215 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 133–173 | 41 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 144–147 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 146–298 | 153 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 151–298 | 148 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 156–287 | 129 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 159–249 | 91 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 177–297 | 115 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 183–258 | 63 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 183–276 | 94 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 194–268 | 54 | 6 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 197–268 | 70 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 222–298 | 77 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 244–267 | 17 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 255–275 | 21 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 274–290 | 11 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 275–284 | 10 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `14` (SAF1)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '14' has invalid range: start=185, end=108. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-294] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-268] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-231] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-267] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [185-229] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-257] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-145] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-263] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-79] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [185-229] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-291] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-173] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-298] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-287] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-237] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-216] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-248] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-257] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-248] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-267] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-275] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-290] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-284] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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