# Play-Annotation-Generator Annotation Review — FieldGoalBlock_138

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_138`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 16
- **Ball Tracks:** 0
- **Action Segments:** 53
- **Validation Warnings:** 68
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 2
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `4` | `4` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `4` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `4` | `4` | 30 | START | 30 | 41 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 52 | START | 52 | 57 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PlaceBall` | 30 | 41 | 12 | inferred_complete_timeline |
| `Action_None` | 42 | 78 | 37 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 120 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_KickBall` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_None` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 120 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 87 | 16 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 75 | 24 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 106 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 120 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 24–103 | 80 | 2 | Undefined position; Undefined team |
| `7` | `9` | Position_Unknown | Team_Unknown | 43–109 | 46 | 5 | Undefined position; Undefined team |
| `8` | `11` | Position_Unknown | Team_Unknown | 57–110 | 22 | 6 | Undefined position; Undefined team |
| `9` | `12` | Position_Unknown | Team_Unknown | 66–70 | 5 | 1 | Undefined position; Undefined team |
| `10` | `13` | Position_Unknown | Team_Unknown | 81–120 | 17 | 3 | Undefined position; Undefined team |
| `11` | `14` | Position_Unknown | Team_Unknown | 82–89 | 6 | 2 | Undefined position; Undefined team |
| `12` | `16` | Position_Unknown | Team_Unknown | 84–93 | 8 | 2 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 98–119 | 21 | 2 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 112–119 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BlockKick' at frame 57 targets track ID '-', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 47 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [58-71] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-78] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-87] for track '5' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-49] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-89] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-89] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.

</details>