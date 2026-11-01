# Play-Annotation-Generator Annotation Review — InsideZoneRead_252

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_252`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 6 | START | 6 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 9 | START | 18 | 62 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 9 | START | 9 | 62 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 9 | START | 9 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 9 | START | 9 | 26 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 9 | START | 9 | 62 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 17 | END | 6 | 17 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 21 | START | 21 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `5` | `4` | 30 | START | 30 | 41 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 47 | START | 47 | 84 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 62 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_None` | 18 | 20 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_Keep` | 30 | 41 | 12 | inferred_complete_timeline |
| `Action_Keep` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 47 | 84 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 74 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 9 | 62 | 54 | inferred_complete_timeline |
| `Action_None` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 9 | 62 | 54 | inferred_complete_timeline |
| `Action_None` | 63 | 82 | 20 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 82 | 20 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 9 | 62 | 54 | inferred_complete_timeline |
| `Action_None` | 63 | 82 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 62 | 31 | inferred_complete_timeline |
| `Action_None` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 65 | 60 | inferred_complete_timeline |
| `Action_None` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 82 | 77 | inferred_complete_timeline |
| `Action_None` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 72 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 84 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 82 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 82 | 77 | inferred_complete_timeline |
| `Action_None` | 92 | 193 | 102 | inferred_complete_timeline |
| `Action_None` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_None` | 223 | 260 | 38 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 82 | 77 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 82 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–83 | 84 | 2 | Undefined position; Undefined team |
| `16` | `28` | Position_Unknown | Team_Unknown | 85–91 | 7 | 1 | Undefined position; Undefined team |
| `17` | `34` | Position_Unknown | Team_Unknown | 86–92 | 7 | 1 | Undefined position; Undefined team |
| `18` | `35` | Position_Unknown | Team_Unknown | 87–97 | 10 | 2 | Undefined position; Undefined team |
| `19` | `36` | Position_Unknown | Team_Unknown | 87–91 | 5 | 1 | Undefined position; Undefined team |
| `20` | `37` | Position_Unknown | Team_Unknown | 88–224 | 72 | 6 | Undefined position; Undefined team |
| `21` | `41` | Position_Unknown | Team_Unknown | 93–184 | 89 | 3 | Undefined position; Undefined team |
| `22` | `42` | Position_Unknown | Team_Unknown | 93–99 | 7 | 1 | Undefined position; Undefined team |
| `23` | `43` | Position_Unknown | Team_Unknown | 93–98 | 6 | 1 | Undefined position; Undefined team |
| `24` | `45` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `25` | `47` | Position_Unknown | Team_Unknown | 158–269 | 108 | 2 | Undefined position; Undefined team |
| `26` | `48` | Position_Unknown | Team_Unknown | 175–269 | 81 | 4 | Undefined position; Undefined team |
| `27` | `51` | Position_Unknown | Team_Unknown | 188–269 | 80 | 2 | Undefined position; Undefined team |
| `28` | `52` | Position_Unknown | Team_Unknown | 192–205 | 14 | 1 | Undefined position; Undefined team |
| `29` | `53` | Position_Unknown | Team_Unknown | 197–269 | 68 | 3 | Undefined position; Undefined team |
| `30` | `55` | Position_Unknown | Team_Unknown | 199–269 | 68 | 2 | Undefined position; Undefined team |
| `31` | `57` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `32` | `61` | Position_Unknown | Team_Unknown | 214–269 | 56 | 1 | Undefined position; Undefined team |
| `33` | `62` | Position_Unknown | Team_Unknown | 214–269 | 53 | 3 | Undefined position; Undefined team |
| `34` | `65` | Position_Unknown | Team_Unknown | 217–258 | 25 | 2 | Undefined position; Undefined team |
| `35` | `69` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `36` | `74` | Position_Unknown | Team_Unknown | 234–269 | 23 | 2 | Undefined position; Undefined team |
| `37` | `75` | Position_Unknown | Team_Unknown | 239–269 | 31 | 1 | Undefined position; Undefined team |
| `38` | `76` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `39` | `77` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |
| `40` | `78` | Position_Unknown | Team_Unknown | 266–268 | 3 | 1 | Undefined position; Undefined team |
| `41` | `79` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `5` (2 segments found)

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
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [6–17], lower_priority='Action_ZoneBlock' annotated_start=9, effective_Action_ZoneBlock_start=18.
- ⚠️ Action 'Action_None' range [6-65] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [30-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [47-84] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [9-26] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-84] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [9-62] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-119] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-253] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-220] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-225] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-248] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-248] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-269] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>