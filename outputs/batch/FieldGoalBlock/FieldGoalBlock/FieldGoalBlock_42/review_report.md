# Play-Annotation-Generator Annotation Review — FieldGoalBlock_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_42`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 94
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
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `15` | `15` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Left_Edge_Rusher | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `15` | `15` | 16 | START | 16 | 29 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 30 | START | 30 | 43 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 54 | START | 54 | 57 |
| ✅ EXACT | `Action_BlockKick` | Left_Edge_Rusher | `6` | `6` | 57 | START | 57 | 61 |

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
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PlaceBall` | 30 | 43 | 14 | inferred_complete_timeline |
| `Action_None` | 44 | 79 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_KickBall` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 58 | 79 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 15 | 7 | inferred_complete_timeline |
| `Action_None` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 88 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 42 | 27 | inferred_complete_timeline |
| `Action_None` | 44 | 66 | 23 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 82 | 67 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_None` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 62 | 22 | inferred_complete_timeline |
| `Action_None` | 64 | 85 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 84 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 81 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_None` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_None` | 59 | 84 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 83 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 91 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 88 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_None` | 51 | 83 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 51 | 36 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 15 | 8 | inferred_complete_timeline |
| `Action_None` | 16 | 19 | 4 | inferred_complete_timeline |
| `Action_None` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_None` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_None` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_None` | 56 | 70 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 71 | 56 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_BlockKick` | 57 | 61 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 34 | 19 | inferred_complete_timeline |
| `Action_None` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 87 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 24–89 | 46 | 5 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 74–77 | 4 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 133–208 | 67 | 7 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 133–210 | 25 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 138–177 | 8 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 145–160 | 14 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 154–157 | 4 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 162–210 | 35 | 5 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 186–191 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [16-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-70] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [57-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-51] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-66] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-54] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 30, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [30-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-54] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-88] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-19] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-76] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '27' has 1 frames without a visible bounding box.
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

</details>