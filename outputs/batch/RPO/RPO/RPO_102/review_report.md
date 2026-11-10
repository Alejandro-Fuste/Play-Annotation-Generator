# Play-Annotation-Generator Annotation Review — RPO_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_102`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 103
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `28` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 5 | START | 5 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 5 | START | 5 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 5 | START | 5 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 5 | START | 5 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 5 | START | 5 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 5 | START | 5 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 5 | START | 5 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 5 | START | 5 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 39 | START | 39 | 59 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 39 | START | 39 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 39 | START | 39 | 52 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 39 | START | 39 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `7` | 39 | START | 39 | 67 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `5` | 55 | START | 55 | 66 |
| ✅ EXACT | `Action_PullBall` | QB | `5` | `5` | 67 | START | 67 | 79 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 96 | START | 96 | 105 |

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
- **Visible Frames:** 5–130
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_ReadDefender` | 55 | 66 | 12 | inferred_complete_timeline |
| `Action_PullBall` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_None` | 80 | 95 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_None` | 106 | 108 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 130 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–230
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 77 | 40 | inferred_complete_timeline |
| `Action_None` | 79 | 223 | 145 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–62
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 15 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_None` | 42 | 62 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–267
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 105 | 67 | inferred_complete_timeline |
| `Action_None` | 106 | 257 | 152 | inferred_complete_timeline |
| `Action_None` | 260 | 267 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–132
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 105 | 67 | inferred_complete_timeline |
| `Action_None` | 106 | 121 | 16 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 59 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 105 | 41 | inferred_complete_timeline |
| `Action_None` | 106 | 195 | 90 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–103
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 103 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 5–52
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 52 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–231
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 231 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–289
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 117 | 80 | inferred_complete_timeline |
| `Action_None` | 121 | 289 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–267
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 242 | 205 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–83
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 77 | 40 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–217
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 217 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 5–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 472 | 435 | inferred_complete_timeline |
| `Action_None` | 476 | 479 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–479
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 117 | 80 | inferred_complete_timeline |
| `Action_None` | 125 | 479 | 355 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 51–198 | 148 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 61–153 | 93 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 81–254 | 169 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 88–246 | 132 | 6 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 95–101 | 7 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 116–388 | 273 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 122–460 | 329 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 122–248 | 126 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 133–387 | 255 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 151–457 | 304 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 154–234 | 46 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 161–181 | 21 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 169–181 | 13 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 181–371 | 191 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 183–191 | 9 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 205–293 | 89 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 273–278 | 6 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 276–479 | 204 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 285–286 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 320–479 | 160 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 433–479 | 42 | 3 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 442–443 | 2 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 458–479 | 22 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 471–472 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `25` | 93 | 97 | 5 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 74 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_None' range [38-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-472] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '5' starts at frame 106, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [106-108] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-242] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-103] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-77] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-257] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-15] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-62] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-254] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-246] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-436] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-456] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-244] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-387] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-421] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-457] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-371] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-191] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-278] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-479] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-447] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-463] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>