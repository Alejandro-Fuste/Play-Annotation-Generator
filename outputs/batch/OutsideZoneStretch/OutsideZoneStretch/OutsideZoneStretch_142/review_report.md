# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_142`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 129
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DT2 | defense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 479 |
| ✅ EXACT | `Action_PressEdge` | RT | `2` | `2` | 182 | START | 182 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DT2 | `15` | `15` | 191 | START | 191 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `10` | 206 | START | 206 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 206 | START | 206 | 234 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 206 | START | 206 | 258 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 206 | START | 206 | 258 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–486
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |
| `Action_PreSnap` | 485 | 486 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 273 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 417 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–459
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 297 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 459 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 258 | 53 | inferred_complete_timeline |
| `Action_None` | 259 | 304 | 46 | inferred_complete_timeline |
| `Action_None` | 313 | 319 | 7 | inferred_complete_timeline |
| `Action_None` | 321 | 424 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 258 | 53 | inferred_complete_timeline |
| `Action_None` | 259 | 303 | 45 | inferred_complete_timeline |
| `Action_None` | 305 | 309 | 5 | inferred_complete_timeline |
| `Action_None` | 311 | 334 | 24 | inferred_complete_timeline |
| `Action_None` | 337 | 509 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 258 | 53 | inferred_complete_timeline |
| `Action_None` | 259 | 425 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PressEdge` | 182 | 205 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 234 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 113 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 157 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 166 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 252 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 70 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 126 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 190 | 183 | inferred_complete_timeline |
| `Action_Handoff` | 191 | 191 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 261 | 14 | inferred_complete_timeline |
| `Action_None` | 263 | 305 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 254 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 292 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 305 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 313 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 266 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 364 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 371 | 509 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 391 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 496 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 508 | 509 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 14 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 232 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 10–40 | 31 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 34–288 | 250 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 163–311 | 110 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 221–408 | 162 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 237–275 | 39 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 244–509 | 259 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 246–509 | 251 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 246–509 | 242 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 254–297 | 30 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 261–340 | 74 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 268–291 | 16 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 289–509 | 207 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 289–343 | 44 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 300–509 | 198 | 4 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 335–509 | 174 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 342–347 | 6 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 352–381 | 28 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 360–386 | 26 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 361–509 | 149 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 364–365 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 375–379 | 4 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 437–471 | 23 | 5 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 438–441 | 4 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 469–488 | 18 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 483–484 | 2 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 488–492 | 5 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 505–506 | 2 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 506–509 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_Handoff` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 128 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-391] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-496] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-364] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [236-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-254] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-292] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-14] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-303] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-334] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-459] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-425] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-479] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-486] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-304] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-424] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-273] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-417] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-137] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-152] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-166] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-172] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '15' starts at frame 191, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [191-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-305] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-280] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-307] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-408] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-275] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-432] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-353] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-425] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-429] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-307] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-366] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-297] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-281] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-293] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-340] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-307] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-343] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-335] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-343] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-503] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-488] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-347] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-376] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-381] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-367] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-386] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-439] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-443] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-454] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-460] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-471] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-441] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-477] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-488] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-484] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-492] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-506] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [506-509] for track '44' has 1 frames without a visible bounding box.
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

</details>