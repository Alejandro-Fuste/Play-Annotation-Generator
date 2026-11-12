# Play-Annotation-Generator Annotation Review — SplitZone_180

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_180`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 23 | START | 24 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 23 | START | 24 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 23 | START | 24 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 23 | START | 28 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 23 | START | 24 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 23 | START | 24 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `7` | `Group` | 23 | START | 24 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 23 | START | 24 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `14` | 42 | START | 42 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 45 | START | 45 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 45 | START | 45 | 103 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 45 | START | 55 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 45 | START | 45 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 45 | START | 45 | 87 |
| ✅ EXACT | `Action_SplitBlock` | HB | `7` | `7` | 49 | START | 49 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 54 | END | 42 | 54 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 58 | START | 58 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `0` | `0` | 68 | START | 68 | 74 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 135 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 24–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 54 | 13 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_None` | 68 | 125 | 58 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 24–128
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 67 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 128 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–88
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 48 | 25 | inferred_complete_timeline |
| `Action_SplitBlock` | 49 | 88 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 24–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 87 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 135 | 46 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 24–73
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 73 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 28–65
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 39 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 54 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 65 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–180
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 59 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 89 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 104 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 135 | 22 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–180
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 44 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 103 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 135 | 1 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–154
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 91 | 50 | inferred_complete_timeline |
| `Action_None` | 93 | 107 | 15 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 154 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–68
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 68 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–180
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 180 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–65
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 103 | 62 | inferred_complete_timeline |
| `Action_None` | 105 | 180 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 24–66
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 66 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 24–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 180 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 73–119 | 47 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 78–180 | 102 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 92–125 | 32 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 103–159 | 53 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 104–180 | 55 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 123–177 | 55 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 126–180 | 45 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 136–180 | 45 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 138–178 | 10 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 142–180 | 39 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 169–180 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 45 != Inferred start 55
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 91 frames exceeds threshold 90 frames [start=45, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 91 frames exceeds threshold 90 frames [start=45, end=135].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 91 frames exceeds threshold 90 frames [start=45, end=135].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [42–54], lower_priority='Action_ZoneBlock' annotated_start=45, effective_Action_ZoneBlock_start=55.
- ⚠️ Action 'Action_BallCarry' range [68-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-103] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-68] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 136, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [136-180] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-32] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [49-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-87] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-32] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-41] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '14' starts at frame 42, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [42-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-143] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '26' has 1 frames without a visible bounding box.
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

</details>