# Play-Annotation-Generator Annotation Review — Duo_236

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_236`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | TE2 | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `22` | `18` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `22` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `10` | `10` | 136 | START | 136 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | TE2 | `2` | `2` | 136 | START | 136 | 155 |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | `22` | `18` | 136 | START | 139 | 163 |
| ✅ EXACT | `Action_ComboBlock` | RT | `3` | `3` | 136 | START | 136 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `22` | `18` | 164 | START | 164 | 198 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 207 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–328
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 328 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 242 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 284 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 328 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 238 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ComboBlock` | 136 | 155 | 20 | inferred_complete_timeline |
| `Action_ComboBlock` | 157 | 197 | 41 | inferred_complete_timeline |
| `Action_ComboBlock` | 199 | 204 | 6 | inferred_complete_timeline |
| `Action_None` | 278 | 328 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 318 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 135 | 129 | inferred_complete_timeline |
| `Action_ComboBlock` | 136 | 187 | 52 | inferred_complete_timeline |
| `Action_ComboBlock` | 191 | 207 | 17 | inferred_complete_timeline |
| `Action_None` | 208 | 249 | 42 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 328 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 244 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 268 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 273 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 135 | 101 | inferred_complete_timeline |
| `Action_ComboBlock` | 136 | 207 | 72 | inferred_complete_timeline |
| `Action_None` | 208 | 241 | 34 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 266 | 18 | inferred_complete_timeline |
| `Action_None` | 283 | 286 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 264 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 324 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 194 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 249 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 269 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 291 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 304 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 328 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 131 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 328 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | Position_Unknown | Team_Unknown | 30–57 | 7 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 61–248 | 132 | 11 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 125–183 | 9 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 170–172 | 3 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 176–328 | 153 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 183–200 | 18 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 211–224 | 10 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 214–246 | 21 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 216–253 | 37 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 219–328 | 88 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 232–254 | 23 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 237–328 | 88 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 316–328 | 12 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 317–328 | 7 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `2` (3 segments found)
- ⚠️ `Action_ComboBlock` for actor_track_id `22` (Position_Unknown): Annotated start 136 != Inferred start 139
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 82 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [136-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [157-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [199-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-266] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-242] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-328] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [136-187] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-249] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-318] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-324] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-179] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-291] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-304] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-328] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-80] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [164-198] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-200] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-224] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-328] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '30' has 1 frames without a visible bounding box.
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