# Play-Annotation-Generator Annotation Review — JetSweep_154

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_154`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 65 | START | 65 | 79 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 67 | START | 80 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 67 | START | 67 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 67 | START | 67 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 67 | START | 67 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 67 | START | 67 | 97 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `21` | `20` | 68 | START | 68 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 79 | END | 65 | 79 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 82 | START | 82 | 89 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `21` | `20` | 90 | START | 90 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 65 | 79 | 15 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_Toss` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 121 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 99 | 35 | inferred_complete_timeline |
| `Action_None` | 102 | 148 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 86 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 109 | 43 | inferred_complete_timeline |
| `Action_None` | 110 | 117 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 94 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 109 | 11 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_BallSnap` | 65 | 79 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 109 | 30 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 90 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 109 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 110 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 97 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 155 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 110 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 119 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 113 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 82 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 299 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 110 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_None` | 65 | 180 | 116 | inferred_complete_timeline |
| `Action_None` | 183 | 219 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–127 | 93 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–114 | 112 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 36–39 | 4 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 68–299 | 232 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 79–99 | 18 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 114–222 | 109 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 120–299 | 180 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 192–225 | 17 | 4 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 199–217 | 14 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 207–299 | 93 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 215–265 | 10 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 226–279 | 29 | 3 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 236–255 | 18 | 2 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 236–241 | 4 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 236–299 | 44 | 3 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 253–256 | 4 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 268–290 | 23 | 1 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `40` | `71` | Position_Unknown | Team_Unknown | 279–299 | 16 | 2 | Undefined position; Undefined team |
| `41` | `73` | Position_Unknown | Team_Unknown | 281–286 | 6 | 1 | Undefined position; Undefined team |
| `42` | `74` | Position_Unknown | Team_Unknown | 282–283 | 2 | 1 | Undefined position; Undefined team |
| `43` | `75` | Position_Unknown | Team_Unknown | 284–285 | 2 | 1 | Undefined position; Undefined team |
| `44` | `76` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `45` | `78` | Position_Unknown | Team_Unknown | 287–298 | 11 | 2 | Undefined position; Undefined team |
| `46` | `79` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 67 != Inferred start 80
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 309: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [65–79], lower_priority='Action_ZoneBlock' annotated_start=67, effective_Action_ZoneBlock_start=80.
- ⚠️ Action 'Action_None' range [65-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 110, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [110-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 110, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [110-113] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-219] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-119] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-127] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-222] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-265] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-247] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-290] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '45' has 1 frames without a visible bounding box.
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

</details>