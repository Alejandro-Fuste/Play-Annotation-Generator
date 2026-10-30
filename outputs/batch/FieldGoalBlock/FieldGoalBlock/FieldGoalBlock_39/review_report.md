# Play-Annotation-Generator Annotation Review — FieldGoalBlock_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_39`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 8 | START | 8 | 22 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 27 | START | 27 | 32 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | `6` | `6` | 32 | START | 32 | 42 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PlaceBall` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_None` | 33 | 120 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_KickBall` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_None` | 33 | 99 | 67 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_None` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_None` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 70 | 44 | inferred_complete_timeline |
| `Action_None` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 117 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 37 | 76 | 40 | inferred_complete_timeline |
| `Action_None` | 81 | 120 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_None` | 42 | 55 | 14 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 63 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 55 | 29 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 54 | 28 | inferred_complete_timeline |
| `Action_None` | 57 | 89 | 33 | inferred_complete_timeline |
| `Action_None` | 91 | 103 | 13 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 120 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 111 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_BlockKick` | 32 | 42 | 11 | inferred_complete_timeline |
| `Action_None` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_None` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 115 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 26 | 1 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 47 | 55 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 17 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 26 | 22 | inferred_complete_timeline |
| `Action_None` | 27 | 120 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 120 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_None` | 37 | 61 | 25 | inferred_complete_timeline |
| `Action_None` | 93 | 115 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–111 | 56 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 52–63 | 8 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 53–55 | 3 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 53–117 | 18 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 76–98 | 9 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 81–120 | 21 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 82–120 | 32 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 85–108 | 16 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 86–110 | 24 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 86–110 | 18 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 101 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [27-54] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-89] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-55] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-39] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-24] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [32-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-47] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-115] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-63] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-111] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-58] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-32] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-55] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-76] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-70] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 27, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [27-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-115] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-40] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 27, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [27-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-114] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-120] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-99] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>