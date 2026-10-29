# Play-Annotation-Generator Annotation Review — Duo_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_35`
- **Frame Range:** 0 to 388 (389 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 388
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | CB2 | defense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | defense | `8` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | defense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 371 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 320 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 388 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 226 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 310 |
| ✅ EXACT | `Action_ComboBlock` | CB2 | `1` | `1` | 164 | START | 164 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `17` | `17` | 164 | START | 164 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `22` | `21` | 164 | START | 164 | 166 |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | `8` | `8` | 164 | START | 164 | 230 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | `7` | `7` | 199 | START | 199 | 219 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 388 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 371 | 372 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 388 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 310 | 311 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 343 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 372 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 319 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 320 | 321 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 355 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 388 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ComboBlock` | 164 | 192 | 29 | inferred_complete_timeline |
| `Action_ComboBlock` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_ComboBlock` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 241 | 388 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 189 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 251 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 185 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 248 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 192 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 249 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 276 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 290 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 334 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 198 | 111 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 199 | 219 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 180 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 209 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 221 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 241 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 205 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 265 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ComboBlock` | 164 | 230 | 67 | inferred_complete_timeline |
| `Action_None` | 231 | 288 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 308 | 309 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 351 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_ComboBlock` | 164 | 230 | 67 | inferred_complete_timeline |
| `Action_None` | 231 | 363 | 133 | inferred_complete_timeline |
| `Action_None` | 367 | 388 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–358 | 359 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–169 | 108 | 13 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 212–340 | 129 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 243–388 | 146 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 266–277 | 12 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 272–304 | 33 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 276–388 | 91 | 5 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 277–293 | 14 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 309–337 | 21 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 321–387 | 60 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 350–388 | 39 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 359–388 | 30 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 367–388 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 72: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 72: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-308] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-351] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-265] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-248] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [199-219] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-363] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-310] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-343] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-372] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-371] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '12' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-320] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-355] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-221] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-241] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-290] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-388] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [164-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [200-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [216-223] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-388] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-189] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-251] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-319] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-73] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [164-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [168-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-340] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-277] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-304] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-343] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-363] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-322] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-387] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>