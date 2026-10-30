# Play-Annotation-Generator Annotation Review — FieldGoalBlock_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 3
- **Group Expanded Events:** 2
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher5 | defense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Left_Edge_Rusher | defense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 5 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 6 | START | 6 | 10 |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher5 | `8` | `8` | 21 | START | 21 | 31 |
| ✅ EXACT | `Action_KickBall` | Left_Edge_Rusher | `1` | `1` | 43 | START | 43 | 49 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `10` | `10` | 45 | START | 45 | 56 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_LongSnap` | 6 | 10 | 5 | inferred_complete_timeline |
| `Action_LongSnap` | 12 | 20 | 9 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 56 | 66 | 11 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 20 | 15 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 94 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 64 | 59 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_None` | 9 | 11 | 3 | inferred_complete_timeline |
| `Action_None` | 15 | 27 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 34 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_None` | 20 | 21 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 10 | 5 | inferred_complete_timeline |
| `Action_None` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 94 | 25 | inferred_complete_timeline |
| `Action_None` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 41 | 36 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PlaceBall` | 21 | 31 | 11 | inferred_complete_timeline |
| `Action_None` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_None` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_None` | 89 | 103 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 120 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 15 | 10 | inferred_complete_timeline |
| `Action_None` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_None` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_None` | 89 | 120 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_KickBall` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_None` | 50 | 72 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 47 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–120 | 121 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–120 | 121 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–120 | 119 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–101 | 75 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–94 | 95 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–61 | 62 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–33 | 34 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 20–53 | 27 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 22–106 | 65 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 25–90 | 30 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 64–80 | 12 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 72–76 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 79–80 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 90–93 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 95–97 | 3 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 100–120 | 21 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 105–108 | 4 | 1 | Undefined position; Undefined team |
| `31` | `59` | Position_Unknown | Team_Unknown | 112–120 | 9 | 1 | Undefined position; Undefined team |
| `32` | `63` | Position_Unknown | Team_Unknown | 114–120 | 4 | 2 | Undefined position; Undefined team |
| `33` | `64` | Position_Unknown | Team_Unknown | 115–120 | 6 | 1 | Undefined position; Undefined team |
| `34` | `67` | Position_Unknown | Team_Unknown | 117–120 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 54: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-47] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-120] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-35] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-79] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-86] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-103] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-20] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-26] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-94] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [6-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 21, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [21-21] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-66] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-17] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-27] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-40] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-91] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-120] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>