# Play-Annotation-Generator Annotation Review — FieldGoalBlock_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_4`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `17` | `17` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | defense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `17` | `17` | 18 | START | 18 | 32 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 33 | START | 33 | 41 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | `9` | `9` | 50 | START | 50 | 88 |
| ✅ EXACT | `Action_KickBall` | Kicker | `6` | `6` | 59 | START | 59 | 65 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PlaceBall` | 33 | 41 | 9 | inferred_complete_timeline |
| `Action_None` | 42 | 90 | 49 | inferred_complete_timeline |
| `Action_None` | 96 | 120 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_KickBall` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_None` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 120 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 39 | 22 | inferred_complete_timeline |
| `Action_None` | 43 | 60 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 113 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 80 | 32 | inferred_complete_timeline |
| `Action_None` | 105 | 120 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 31 | 14 | inferred_complete_timeline |
| `Action_None` | 99 | 109 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 118 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 18 | 32 | 15 | inferred_complete_timeline |
| `Action_None` | 33 | 120 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 43 | 26 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 102 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 34 | 17 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 102 | 115 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 65 | 48 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 46 | 29 | inferred_complete_timeline |
| `Action_None` | 108 | 120 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 120 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 120 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 54 | 37 | inferred_complete_timeline |
| `Action_None` | 56 | 76 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_None` | 60 | 120 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BlockKick` | 50 | 88 | 39 | inferred_complete_timeline |
| `Action_None` | 89 | 120 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 56 | 39 | inferred_complete_timeline |
| `Action_None` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_None` | 68 | 120 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 120 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 60 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 120 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 120 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 8–120 | 23 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 28–118 | 88 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 84–87 | 4 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 96–118 | 20 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 97–120 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_End` position mapped to `offense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [18-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-120] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-76] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-39] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-115] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-65] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-31] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-109] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-80] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-120] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-118] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-120] for track '25' has 2 frames without a visible bounding box.
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

</details>