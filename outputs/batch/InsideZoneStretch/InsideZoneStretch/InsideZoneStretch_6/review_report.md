# Play-Annotation-Generator Annotation Review — InsideZoneStretch_6

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `InsideZoneStretch_6`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_InsideZoneStretch`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 152
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PressGap` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 123 | START | 123 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `0` | `0` | 136 | START | 136 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 136 | START | 136 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `15` | 136 | START | 136 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 136 | START | 136 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 136 | START | 136 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `15` | `15` | 142 | START | 142 | 173 |
| ✅ EXACT | `Action_PressGap` | RB | `13` | `13` | 152 | START | 152 | 171 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `19` | `17` | 159 | START | 159 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `13` | 172 | START | 172 | 182 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 27 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 106 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 151 | 12 | inferred_complete_timeline |
| `Action_PressGap` | 152 | 171 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 182 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 218 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 296 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 167 | 45 | inferred_complete_timeline |
| `Action_None` | 184 | 201 | 18 | inferred_complete_timeline |
| `Action_None` | 214 | 291 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 90 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 135 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 142 | 173 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 293 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 120 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 126 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 136 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_None` | 175 | 287 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_BallSnap` | 123 | 123 | 1 | inferred_complete_timeline |
| `Action_None` | 124 | 135 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_None` | 175 | 300 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 174 | 39 | inferred_complete_timeline |
| `Action_None` | 175 | 203 | 29 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 174 | 39 | inferred_complete_timeline |
| `Action_None` | 175 | 303 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 202 | 80 | inferred_complete_timeline |
| `Action_None` | 206 | 266 | 61 | inferred_complete_timeline |
| `Action_None` | 271 | 277 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 122 | 9 | inferred_complete_timeline |
| `Action_None` | 123 | 254 | 132 | inferred_complete_timeline |
| `Action_None` | 258 | 265 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 155 | 33 | inferred_complete_timeline |
| `Action_None` | 158 | 389 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 277 | 155 | inferred_complete_timeline |
| `Action_None` | 279 | 289 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 176 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–364
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 236 | 114 | inferred_complete_timeline |
| `Action_None` | 239 | 364 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 216 | 94 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_None` | 167 | 185 | 19 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 202 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 273 | 151 | inferred_complete_timeline |
| `Action_None` | 277 | 284 | 8 | inferred_complete_timeline |
| `Action_None` | 286 | 321 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 136–269 | 134 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 136–206 | 63 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 166–213 | 27 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 175–281 | 107 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 190–316 | 127 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 191–238 | 47 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 209–321 | 67 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 214–389 | 174 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 214–389 | 176 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 215–259 | 45 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 223–231 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 225–274 | 50 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 226–231 | 6 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 228–327 | 97 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 230–271 | 42 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 237–255 | 4 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 250–273 | 19 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 264–340 | 74 | 3 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 275–335 | 61 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 297–389 | 86 | 3 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 310–389 | 80 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 382–389 | 8 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SnapReceive' at frame 129 targets track ID '?', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 96 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_BallSnap present in CSV, but paired Action_SnapReceive is missing.
- ⚠️ Action 'Action_None' range [175-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-216] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-364] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-277] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-289] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-303] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-300] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-106] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-21] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [142-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-135] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '16' starts at frame 136, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [136-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-287] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-316] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-251] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-340] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-389] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-295] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-327] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-271] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-263] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-279] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-312] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-340] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-335] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-350] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '43' has 1 frames without a visible bounding box.
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

</details>