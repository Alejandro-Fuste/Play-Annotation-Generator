# Play-Annotation-Generator Annotation Review — InsideZoneRead_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_48`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 175 | START | 175 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 178 | START | 178 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 178 | START | 178 | 253 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 178 | START | 194 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 178 | START | 178 | 202 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `9` | `8` | 178 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | RB | `10` | `9` | 191 | END | 175 | 191 |
| ✅ EXACT | `Action_ReadDefender` | RB | `10` | `9` | 198 | START | 198 | 208 |
| ✅ EXACT | `Action_Handoff` | RB | `10` | `9` | 209 | START | 209 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 225 | START | 225 | 286 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 261 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 224 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 225 | 286 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 295 | 369 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_SnapReceive` | 175 | 191 | 17 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 198 | 208 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 209 | 224 | 16 | inferred_complete_timeline |
| `Action_None` | 225 | 231 | 7 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–311
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 10 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 177 | 158 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 253 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 311 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 77 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 177 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 191 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_BallSnap` | 175 | 185 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 220 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 224 | 232 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 261 | 24 | inferred_complete_timeline |
| `Action_None` | 262 | 282 | 21 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 290 | 305 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_ZoneBlock` | 178 | 202 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 261 | 49 | inferred_complete_timeline |
| `Action_None` | 262 | 275 | 14 | inferred_complete_timeline |
| `Action_None` | 277 | 331 | 55 | inferred_complete_timeline |
| `Action_None` | 333 | 354 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_None` | 175 | 229 | 55 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_None` | 175 | 187 | 13 | inferred_complete_timeline |
| `Action_None` | 189 | 257 | 69 | inferred_complete_timeline |
| `Action_None` | 271 | 296 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 174 | 123 | inferred_complete_timeline |
| `Action_None` | 175 | 301 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 174 | 154 | inferred_complete_timeline |
| `Action_None` | 175 | 231 | 57 | inferred_complete_timeline |
| `Action_None` | 233 | 304 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_None` | 175 | 262 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_None` | 175 | 229 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 46–320 | 233 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 63–64 | 2 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 195–294 | 98 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 227–247 | 21 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 234–243 | 10 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 256–266 | 11 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 256–307 | 52 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 265–279 | 15 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 273–308 | 36 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 286–479 | 175 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 292–324 | 27 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 294–359 | 56 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 300–470 | 145 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 303–479 | 167 | 6 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 309–479 | 161 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 338–370 | 32 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 346–465 | 119 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 380–467 | 75 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 419–430 | 12 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 439–479 | 36 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 448–459 | 12 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 468–470 | 3 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 474–479 | 6 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (RG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=178, end=33. Clamping end to start.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [175–191], lower_priority='Action_ZoneBlock' annotated_start=178, effective_Action_ZoneBlock_start=192.
- ⚠️ Action 'Action_None' range [175-229] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-275] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-331] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-354] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-257] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-296] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [295-369] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [373-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-46] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-82] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-90] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-177] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '10' starts at frame 178, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [178-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-231] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [178-253] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [259-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-311] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [175-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-220] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [224-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-305] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-232] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-320] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-247] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-307] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-308] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-410] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-437] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-324] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-335] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-417] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-450] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-352] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-380] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-391] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-435] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-415] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-367] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-380] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-465] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-386] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-467] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-430] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-450] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-479] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-459] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>