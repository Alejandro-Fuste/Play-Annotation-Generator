# Play-Annotation-Generator Annotation Review — OutsideZoneRead_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_49`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 49
- **Ball Tracks:** 2
- **Action Segments:** 100
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | DE1 | defense | `2` | `2` |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR1 | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | WR1 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 257 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 240 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `14` | 191 | START | 191 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 191 | START | 191 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 191 | START | 191 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 191 | START | 191 | 244 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 191 | START | 191 | 244 |
| ✅ EXACT | `Action_PressEdge` | DE1 | `2` | `2` | 200 | START | 200 | 255 |
| ✅ EXACT | `Action_ReadEdgeDefender` | WR1 | `7` | `7` | 203 | START | 203 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | WR1 | `7` | `7` | 227 | START | 227 | 235 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 302 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 437 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 460 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 473 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 475 | 479 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 203 | 213 | 11 | inferred_complete_timeline |
| `Action_None` | 214 | 226 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 258 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 257 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 244 | 54 | inferred_complete_timeline |
| `Action_None` | 245 | 369 | 125 | inferred_complete_timeline |
| `Action_None` | 375 | 479 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 244 | 54 | inferred_complete_timeline |
| `Action_None` | 245 | 454 | 210 | inferred_complete_timeline |
| `Action_None` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 244 | 54 | inferred_complete_timeline |
| `Action_None` | 245 | 330 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 244 | 54 | inferred_complete_timeline |
| `Action_None` | 245 | 279 | 35 | inferred_complete_timeline |
| `Action_None` | 281 | 479 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 191 | 244 | 54 | inferred_complete_timeline |
| `Action_None` | 245 | 245 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PressEdge` | 200 | 255 | 56 | inferred_complete_timeline |
| `Action_None` | 256 | 276 | 21 | inferred_complete_timeline |
| `Action_None` | 318 | 328 | 11 | inferred_complete_timeline |
| `Action_None` | 330 | 479 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 379 | 380 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 397 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 479 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 300 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 298 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 479 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 479 | 480 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 115 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 156 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 21–108 | 32 | 7 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 88–93 | 4 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 199–479 | 281 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 225–479 | 255 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 231–362 | 83 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 254–345 | 92 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 266–479 | 214 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 306–479 | 170 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 306–479 | 173 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 308–309 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 342–368 | 27 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 354–368 | 15 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 361–368 | 8 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 369–479 | 111 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 369–479 | 111 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 369–479 | 111 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 376–479 | 104 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 378–383 | 4 | 2 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 385–479 | 95 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 387–415 | 22 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 390–479 | 90 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 395–418 | 20 | 3 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 425–454 | 30 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 426–479 | 54 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 428–439 | 6 | 2 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 435–440 | 6 | 1 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 454–479 | 12 | 2 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 475–476 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | 0 | 53 | 54 | 100.0% | None |
| `22` | `26` | 138 | 209 | 72 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_Handoff` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 73 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-479] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-302] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-437] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-460] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-473] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-369] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [227-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-379] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-397] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-479] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-257] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-300] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-298] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-454] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 245, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [245-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-330] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-108] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-479] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-345] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-479] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-409] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-332] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-368] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-368] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-368] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-479] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-406] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-415] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-479] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-410] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-418] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-454] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-479] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-439] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-440] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-459] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-476] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>