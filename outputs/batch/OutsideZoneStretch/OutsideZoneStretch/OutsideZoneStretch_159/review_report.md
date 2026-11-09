# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_159`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 56
- **Ball Tracks:** 11
- **Action Segments:** 114
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `0` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `0` | `0` | 180 | START | 180 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `10` | 180 | START | 180 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 180 | START | 180 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 180 | START | 180 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 180 | START | 180 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `13` | `13` | 189 | START | 189 | 198 |
| ✅ EXACT | `Action_Handoff` | RB | `13` | `13` | 199 | START | 199 | 209 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PressEdge` | 189 | 198 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_PressEdge` | 210 | 233 | 24 | inferred_complete_timeline |
| `Action_None` | 234 | 482 | 249 | inferred_complete_timeline |
| `Action_None` | 491 | 497 | 7 | inferred_complete_timeline |
| `Action_None` | 500 | 509 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 195 | 224 | 30 | inferred_complete_timeline |
| `Action_None` | 225 | 352 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 224 | 45 | inferred_complete_timeline |
| `Action_None` | 225 | 275 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 195 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 224 | 28 | inferred_complete_timeline |
| `Action_None` | 225 | 240 | 16 | inferred_complete_timeline |
| `Action_None` | 242 | 248 | 7 | inferred_complete_timeline |
| `Action_None` | 250 | 260 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 224 | 45 | inferred_complete_timeline |
| `Action_None` | 225 | 256 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 199 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 211 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 217 | 224 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 273 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 258 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 255 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 491 | 492 | inferred_complete_timeline |
| `Action_PreSnap` | 494 | 499 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 504 | 509 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 408 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 415 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 419 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 423 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 40–264 | 225 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 181–251 | 71 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 196–214 | 19 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 223–269 | 47 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 252–373 | 121 | 2 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 254–322 | 69 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 268–415 | 136 | 6 | Undefined position; Undefined team |
| `27` | `49` | Position_Unknown | Team_Unknown | 302–372 | 71 | 1 | Undefined position; Undefined team |
| `28` | `53` | Position_Unknown | Team_Unknown | 319–435 | 112 | 3 | Undefined position; Undefined team |
| `29` | `54` | Position_Unknown | Team_Unknown | 321–456 | 136 | 1 | Undefined position; Undefined team |
| `30` | `55` | Position_Unknown | Team_Unknown | 325–382 | 58 | 1 | Undefined position; Undefined team |
| `31` | `58` | Position_Unknown | Team_Unknown | 328–509 | 174 | 4 | Undefined position; Undefined team |
| `32` | `61` | Position_Unknown | Team_Unknown | 332–461 | 128 | 3 | Undefined position; Undefined team |
| `33` | `62` | Position_Unknown | Team_Unknown | 338–382 | 44 | 2 | Undefined position; Undefined team |
| `36` | `67` | Position_Unknown | Team_Unknown | 366–384 | 16 | 2 | Undefined position; Undefined team |
| `37` | `71` | Position_Unknown | Team_Unknown | 383–399 | 13 | 2 | Undefined position; Undefined team |
| `38` | `81` | Position_Unknown | Team_Unknown | 396–509 | 103 | 3 | Undefined position; Undefined team |
| `40` | `98` | Position_Unknown | Team_Unknown | 415–479 | 37 | 4 | Undefined position; Undefined team |
| `42` | `105` | Position_Unknown | Team_Unknown | 430–437 | 6 | 2 | Undefined position; Undefined team |
| `43` | `108` | Position_Unknown | Team_Unknown | 435–438 | 4 | 1 | Undefined position; Undefined team |
| `44` | `109` | Position_Unknown | Team_Unknown | 436–472 | 20 | 4 | Undefined position; Undefined team |
| `45` | `111` | Position_Unknown | Team_Unknown | 439–500 | 62 | 1 | Undefined position; Undefined team |
| `46` | `112` | Position_Unknown | Team_Unknown | 440–455 | 15 | 2 | Undefined position; Undefined team |
| `47` | `119` | Position_Unknown | Team_Unknown | 447–453 | 7 | 1 | Undefined position; Undefined team |
| `49` | `130` | Position_Unknown | Team_Unknown | 457–458 | 2 | 1 | Undefined position; Undefined team |
| `50` | `131` | Position_Unknown | Team_Unknown | 457–458 | 2 | 1 | Undefined position; Undefined team |
| `52` | `135` | Position_Unknown | Team_Unknown | 463–465 | 3 | 1 | Undefined position; Undefined team |
| `55` | `141` | Position_Unknown | Team_Unknown | 476–480 | 5 | 1 | Undefined position; Undefined team |
| `57` | `145` | Position_Unknown | Team_Unknown | 480–484 | 5 | 1 | Undefined position; Undefined team |
| `58` | `147` | Position_Unknown | Team_Unknown | 484–495 | 8 | 2 | Undefined position; Undefined team |
| `59` | `149` | Position_Unknown | Team_Unknown | 487–489 | 3 | 1 | Undefined position; Undefined team |
| `60` | `150` | Position_Unknown | Team_Unknown | 499–502 | 4 | 1 | Undefined position; Undefined team |
| `61` | `151` | Position_Unknown | Team_Unknown | 499–509 | 8 | 2 | Undefined position; Undefined team |
| `62` | `153` | Position_Unknown | Team_Unknown | 499–509 | 11 | 1 | Undefined position; Undefined team |
| `63` | `154` | Position_Unknown | Team_Unknown | 501–502 | 2 | 1 | Undefined position; Undefined team |
| `64` | `155` | Position_Unknown | Team_Unknown | 501–502 | 2 | 1 | Undefined position; Undefined team |
| `65` | `156` | Position_Unknown | Team_Unknown | 502–505 | 4 | 1 | Undefined position; Undefined team |
| `66` | `158` | Position_Unknown | Team_Unknown | 505–509 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 74 | 169 | 79 | 82.3% | 76, 78–84, 87, 89–94, 111–112 |
| `26` | `48` | 299 | 300 | 2 | 100.0% | None |
| `34` | `63` | 342 | 342 | 1 | 100.0% | None |
| `35` | `65` | 351 | 351 | 1 | 100.0% | None |
| `39` | `89` | 402 | 402 | 1 | 100.0% | None |
| `41` | `99` | 416 | 416 | 1 | 100.0% | None |
| `48` | `129` | 457 | 457 | 1 | 100.0% | None |
| `51` | `132` | 459 | 461 | 3 | 100.0% | None |
| `53` | `136` | 464 | 464 | 1 | 100.0% | None |
| `54` | `139` | 467 | 467 | 1 | 100.0% | None |
| `56` | `143` | 478 | 478 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 96 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [180-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-408] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-415] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-423] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-352] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-491] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [494-499] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-275] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-255] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-241] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-482] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-497] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-370] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-322] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-325] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-349] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-415] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-372] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-426] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-432] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-435] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-456] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-382] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-484] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-491] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-501] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-373] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-461] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-379] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-382] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-377] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-384] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-386] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-399] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-485] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-495] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-419] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-424] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-470] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-479] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-437] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-438] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-452] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-458] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-472] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-500] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-441] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-455] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-453] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-458] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-458] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-465] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-480] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-484] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-487] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-495] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-489] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-502] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-504] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [499-509] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-502] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-502] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-505] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
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

</details>