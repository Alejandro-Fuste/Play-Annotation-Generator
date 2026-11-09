# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_23`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 172
- **Validation Warnings:** 220
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 136
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | Position_Unknown | Team_Unknown | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 99 | START | 99 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `10` | 99 | START | 99 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 99 | START | 99 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 99 | START | 99 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `9` | 99 | START | 99 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `16` | `16` | 102 | START | 102 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | Position_Unknown | `17` | `17` | 116 | START | 116 | 118 |

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
- **Visible Frames:** 0–449
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 449 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PressEdge` | 102 | 116 | 15 | inferred_complete_timeline |
| `Action_PressEdge` | 121 | 152 | 32 | inferred_complete_timeline |
| `Action_None` | 153 | 179 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–429
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 194 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 228 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 243 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 274 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 296 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 302 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 330 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 397 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 420 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 429 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 231 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 134 | 36 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |
| `Action_None` | 164 | 381 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 101 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–394
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 134 | 19 | inferred_complete_timeline |
| `Action_None` | 135 | 155 | 21 | inferred_complete_timeline |
| `Action_None` | 164 | 391 | 228 | inferred_complete_timeline |
| `Action_None` | 393 | 394 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 134 | 36 | inferred_complete_timeline |
| `Action_None` | 135 | 356 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 197 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 427 | 428 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 449 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 61 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 103 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 449 | 345 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 166 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 355 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 449 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 238 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 274 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 289 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 323 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 356 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 360 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 296 | 297 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 333 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 449 | 294 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 5–449 | 409 | 8 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 100–140 | 32 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 145–153 | 9 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 156–352 | 197 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 164–384 | 219 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 211–224 | 10 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 211–395 | 181 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 219–449 | 231 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 240–350 | 106 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 245–262 | 6 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 249–407 | 127 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 279–405 | 103 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 280–329 | 46 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 288–378 | 37 | 7 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 290–340 | 43 | 5 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 292–397 | 58 | 6 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 313–423 | 105 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 314–315 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 317–417 | 61 | 6 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 333–336 | 4 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 366–449 | 84 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 367–378 | 9 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 385–386 | 2 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 392–449 | 58 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 395–437 | 40 | 3 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 400–449 | 38 | 7 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 403–412 | 7 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 405–449 | 45 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 413–449 | 37 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 419–449 | 11 | 2 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 426–443 | 12 | 3 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 147 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [135-356] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-296] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-301] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-238] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-323] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-356] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-360] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-243] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-296] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-330] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-397] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-420] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-381] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-355] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-427] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-61] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-391] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-449] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [102-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [116-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-449] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-352] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-374] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-384] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-395] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-227] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-344] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-362] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-395] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-407] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-359] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-373] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-405] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-289] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-324] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-293] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-334] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-349] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-301] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-309] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-300] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-397] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-319] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-415] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-423] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-343] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-372] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-417] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-371] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-386] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-416] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-429] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-437] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-413] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-416] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-420] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-431] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-435] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-438] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-407] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-412] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-428] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-431] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-443] for track '50' has 2 frames without a visible bounding box.
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

</details>