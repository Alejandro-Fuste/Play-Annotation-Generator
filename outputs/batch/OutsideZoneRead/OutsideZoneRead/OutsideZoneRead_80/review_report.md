# Play-Annotation-Generator Annotation Review — OutsideZoneRead_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_80`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 72
- **Ball Tracks:** 1
- **Action Segments:** 132
- **Validation Warnings:** 225
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `12` | `12` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 429 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 125 | START | 125 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 125 | START | 125 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 125 | START | 125 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 125 | START | 125 | 173 |
| ✅ EXACT | `Action_ZoneBlock` | C | `4` | `4` | 125 | START | 125 | 173 |
| ✅ EXACT | `Action_PressEdge` | RB | `12` | `12` | 132 | START | 132 | 187 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `11` | 136 | START | 136 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `11` | `11` | 143 | START | 143 | 147 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 149 | 155 | 7 | inferred_complete_timeline |
| `Action_None` | 156 | 178 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PressEdge` | 132 | 187 | 56 | inferred_complete_timeline |
| `Action_None` | 188 | 491 | 304 | inferred_complete_timeline |
| `Action_None` | 494 | 509 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 279 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 285 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–429
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 429 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 148 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 173 | 24 | inferred_complete_timeline |
| `Action_None` | 174 | 225 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 173 | 49 | inferred_complete_timeline |
| `Action_None` | 174 | 244 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 173 | 49 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 155 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 164 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 222 | 49 | inferred_complete_timeline |
| `Action_None` | 229 | 242 | 14 | inferred_complete_timeline |
| `Action_None` | 320 | 368 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 173 | 49 | inferred_complete_timeline |
| `Action_None` | 174 | 384 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 302 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 306 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 277 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 405 | 406 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 175 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 276 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–422 | 423 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 48–77 | 30 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 112–124 | 13 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–509 | 382 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 164–260 | 97 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 178–189 | 8 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 187–189 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 202–354 | 150 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 205–385 | 176 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 219–229 | 11 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 240–283 | 39 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 262–287 | 12 | 4 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 263–307 | 45 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 263–278 | 14 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 273–286 | 14 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 275–278 | 4 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 280–338 | 32 | 3 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 283–286 | 4 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 283–285 | 3 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 283–347 | 26 | 3 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 284–349 | 33 | 4 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 302–428 | 127 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 314–400 | 85 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 316–474 | 159 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 317–433 | 117 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 318–356 | 5 | 2 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 318–354 | 30 | 5 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 324–350 | 27 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 329–378 | 50 | 1 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 331–442 | 112 | 1 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 331–373 | 41 | 3 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 335–509 | 172 | 2 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 340–360 | 10 | 3 | Undefined position; Undefined team |
| `55` | `74` | Position_Unknown | Team_Unknown | 343–350 | 7 | 2 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 347–352 | 6 | 1 | Undefined position; Undefined team |
| `57` | `77` | Position_Unknown | Team_Unknown | 347–364 | 16 | 2 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 348–356 | 9 | 1 | Undefined position; Undefined team |
| `59` | `81` | Position_Unknown | Team_Unknown | 358–362 | 5 | 1 | Undefined position; Undefined team |
| `60` | `82` | Position_Unknown | Team_Unknown | 361–379 | 19 | 1 | Undefined position; Undefined team |
| `61` | `84` | Position_Unknown | Team_Unknown | 363–364 | 2 | 1 | Undefined position; Undefined team |
| `62` | `86` | Position_Unknown | Team_Unknown | 376–385 | 10 | 1 | Undefined position; Undefined team |
| `63` | `88` | Position_Unknown | Team_Unknown | 392–509 | 118 | 1 | Undefined position; Undefined team |
| `64` | `90` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `65` | `93` | Position_Unknown | Team_Unknown | 414–417 | 4 | 1 | Undefined position; Undefined team |
| `66` | `94` | Position_Unknown | Team_Unknown | 414–509 | 76 | 2 | Undefined position; Undefined team |
| `67` | `95` | Position_Unknown | Team_Unknown | 414–424 | 11 | 1 | Undefined position; Undefined team |
| `68` | `98` | Position_Unknown | Team_Unknown | 483–486 | 4 | 1 | Undefined position; Undefined team |
| `69` | `99` | Position_Unknown | Team_Unknown | 493–496 | 4 | 1 | Undefined position; Undefined team |
| `70` | `100` | Position_Unknown | Team_Unknown | 494–509 | 16 | 1 | Undefined position; Undefined team |
| `71` | `103` | Position_Unknown | Team_Unknown | 501–509 | 9 | 1 | Undefined position; Undefined team |
| `72` | `104` | Position_Unknown | Team_Unknown | 508–509 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 21 | 116 | 67 | 69.8% | 43, 45, 47–54, 82–83, 86–102 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 114 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-422] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-175] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-405] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-302] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-384] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [143-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-491] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-155] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-222] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-368] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-279] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-285] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-429] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-173] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-244] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-189] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-354] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-325] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-341] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-263] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-307] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-273] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-286] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-300] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-334] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-338] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-286] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-285] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-287] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-293] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-347] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-288] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-338] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-349] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-428] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-400] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-474] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-433] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-320] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-332] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-340] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-354] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-350] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-378] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-442] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-344] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-360] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-373] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-419] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-509] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-360] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-347] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-352] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-357] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-364] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-356] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-362] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-379] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-364] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-385] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-509] for track '63' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-417] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-476] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-424] for track '67' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-486] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-496] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>