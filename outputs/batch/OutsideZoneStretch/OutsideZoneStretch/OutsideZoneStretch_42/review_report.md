# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_42`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 77
- **Ball Tracks:** 0
- **Action Segments:** 255
- **Validation Warnings:** 360
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
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 242
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 194 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 326 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 247 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 153 | START | 153 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `3` | `3` | 164 | START | 164 | 179 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 175 | START | 175 | 188 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_Handoff` | 175 | 188 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 374 | 186 | inferred_complete_timeline |
| `Action_None` | 376 | 379 | 4 | inferred_complete_timeline |
| `Action_None` | 381 | 404 | 24 | inferred_complete_timeline |
| `Action_None` | 406 | 419 | 14 | inferred_complete_timeline |
| `Action_None` | 424 | 449 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PressEdge` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_PressEdge` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_PressEdge` | 188 | 212 | 25 | inferred_complete_timeline |
| `Action_None` | 213 | 226 | 14 | inferred_complete_timeline |
| `Action_None` | 231 | 233 | 3 | inferred_complete_timeline |
| `Action_None` | 239 | 449 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–446
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 269 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 446 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–364
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 326 | 327 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 364 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 449 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 218 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 410 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–310
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 310 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 351 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 449 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–12 | 12 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–407 | 357 | 11 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 153–210 | 27 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 158–449 | 169 | 16 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 172–449 | 212 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 198–229 | 31 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 202–413 | 211 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 206–449 | 154 | 29 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 208–222 | 13 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 220–273 | 49 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 221–449 | 220 | 7 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 232–446 | 202 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 234–449 | 200 | 6 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 235–289 | 52 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 236–449 | 191 | 6 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 239–328 | 76 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 240–449 | 207 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 242–447 | 206 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 247–448 | 198 | 4 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 249–258 | 9 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 250–436 | 185 | 2 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 255–261 | 7 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 257–449 | 189 | 4 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 278–354 | 31 | 7 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 281–283 | 3 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 282–342 | 56 | 3 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 296–303 | 7 | 2 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 301–302 | 2 | 1 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 303–309 | 6 | 2 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 312–326 | 15 | 1 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 315–449 | 116 | 6 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 333–449 | 63 | 10 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 334–441 | 102 | 2 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 339–421 | 25 | 5 | Undefined position; Undefined team |
| `51` | `63` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `52` | `64` | Position_Unknown | Team_Unknown | 343–401 | 52 | 5 | Undefined position; Undefined team |
| `53` | `65` | Position_Unknown | Team_Unknown | 347–370 | 6 | 2 | Undefined position; Undefined team |
| `54` | `66` | Position_Unknown | Team_Unknown | 352–361 | 8 | 2 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 356–358 | 3 | 1 | Undefined position; Undefined team |
| `56` | `70` | Position_Unknown | Team_Unknown | 356–357 | 2 | 1 | Undefined position; Undefined team |
| `57` | `71` | Position_Unknown | Team_Unknown | 360–449 | 78 | 4 | Undefined position; Undefined team |
| `58` | `75` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `59` | `76` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `60` | `77` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |
| `61` | `78` | Position_Unknown | Team_Unknown | 380–382 | 3 | 1 | Undefined position; Undefined team |
| `62` | `81` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |
| `63` | `84` | Position_Unknown | Team_Unknown | 392–393 | 2 | 1 | Undefined position; Undefined team |
| `64` | `86` | Position_Unknown | Team_Unknown | 392–437 | 26 | 5 | Undefined position; Undefined team |
| `65` | `87` | Position_Unknown | Team_Unknown | 394–397 | 4 | 1 | Undefined position; Undefined team |
| `66` | `89` | Position_Unknown | Team_Unknown | 396–397 | 2 | 1 | Undefined position; Undefined team |
| `67` | `90` | Position_Unknown | Team_Unknown | 400–401 | 2 | 1 | Undefined position; Undefined team |
| `68` | `91` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `69` | `92` | Position_Unknown | Team_Unknown | 408–448 | 38 | 2 | Undefined position; Undefined team |
| `70` | `96` | Position_Unknown | Team_Unknown | 416–447 | 15 | 2 | Undefined position; Undefined team |
| `71` | `100` | Position_Unknown | Team_Unknown | 420–445 | 23 | 3 | Undefined position; Undefined team |
| `72` | `103` | Position_Unknown | Team_Unknown | 426–449 | 20 | 2 | Undefined position; Undefined team |
| `73` | `105` | Position_Unknown | Team_Unknown | 427–431 | 5 | 1 | Undefined position; Undefined team |
| `74` | `106` | Position_Unknown | Team_Unknown | 428–435 | 8 | 1 | Undefined position; Undefined team |
| `75` | `107` | Position_Unknown | Team_Unknown | 428–449 | 10 | 4 | Undefined position; Undefined team |
| `76` | `109` | Position_Unknown | Team_Unknown | 438–449 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 61 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 61 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 122 |
| Missing visible bounding boxes during action | 237 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-449] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-351] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [164-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [182-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-211] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-374] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-404] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-419] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-446] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-410] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-326] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-364] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-224] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-243] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-303] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-312] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-398] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-404] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-336] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-374] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-391] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-402] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-412] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-418] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-426] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-434] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-442] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-371] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-410] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-232] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-244] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-289] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-312] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-331] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-336] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-349] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-368] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-375] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-390] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-406] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-414] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-418] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-426] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-442] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-259] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-266] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-324] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-362] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-409] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-417] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-442] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-244] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-252] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-348] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-446] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-312] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-399] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-415] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-449] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-289] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-386] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-395] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-404] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-408] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-295] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-307] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-250] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-449] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-447] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-445] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-252] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-258] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-394] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-436] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-261] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-342] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-371] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-429] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-280] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-290] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-305] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-310] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-316] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-296] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-336] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-342] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-300] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-302] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-326] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-368] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-374] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-387] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-399] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-439] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-344] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-357] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-371] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-390] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-406] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-414] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-423] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-433] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-441] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-351] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-441] for track '49' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-391] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-400] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-411] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-421] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-379] for track '52' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-393] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-397] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-370] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-357] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-410] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-417] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-426] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-382] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-389] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-411] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-421] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-437] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-397] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-397] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-409] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-443] for track '69' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-426] for track '70' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-447] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-434] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-441] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-445] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-442] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-431] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-435] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-430] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-442] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-447] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-440] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-449] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.

</details>