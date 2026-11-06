# Play-Annotation-Generator Annotation Review — OutsideZoneRead_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_85`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 106
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
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 328 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 173 | START | 173 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 173 | START | 173 | 176 |
| ✅ EXACT | `Action_PressEdge` | RB | `7` | `7` | 180 | START | 180 | 219 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `10` | `10` | 187 | START | 187 | 190 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 191 | START | 191 | 206 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 191 | 206 | 16 | inferred_complete_timeline |
| `Action_None` | 207 | 359 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PressEdge` | 180 | 219 | 40 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 359 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 74 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 172 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 222 | 40 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 255 | 6 | inferred_complete_timeline |
| `Action_None` | 257 | 273 | 17 | inferred_complete_timeline |
| `Action_None` | 299 | 302 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 359 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 172 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 222 | 35 | inferred_complete_timeline |
| `Action_None` | 226 | 233 | 8 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |
| `Action_None` | 246 | 255 | 10 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 269 | 359 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 255 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 337 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 359 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 4–251 | 96 | 13 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 4–235 | 132 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 64–359 | 156 | 11 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 71–74 | 4 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 148–211 | 30 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 189–359 | 171 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 190–359 | 158 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 229–359 | 131 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 229–359 | 118 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 265–359 | 90 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 268–359 | 92 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 281–359 | 79 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 309–359 | 51 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 343–359 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 77 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-337] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-74] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-222] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-74] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-154] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-161] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-74] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-165] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-215] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-222] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-284] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-319] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-359] for track '27' has 2 frames without a visible bounding box.
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

</details>