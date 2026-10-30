# Play-Annotation-Generator Annotation Review — FieldGoalBlock_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_3`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 87
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
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `20` | `20` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockKick` | Right_End | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `14` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `20` | `20` | 4 | START | 4 | 20 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `8` | `8` | 21 | START | 21 | 34 |
| ✅ EXACT | `Action_KickBall` | Kicker | `11` | `11` | 46 | START | 46 | 53 |
| ✅ EXACT | `Action_BlockKick` | Right_End | `14` | `14` | 54 | START | 54 | 61 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PlaceBall` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_None` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_None` | 55 | 120 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_KickBall` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_None` | 54 | 120 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_None` | 37 | 75 | 39 | inferred_complete_timeline |
| `Action_None` | 77 | 120 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_None` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_None` | 26 | 36 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_None` | 35 | 49 | 15 | inferred_complete_timeline |
| `Action_None` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_None` | 90 | 108 | 19 | inferred_complete_timeline |
| `Action_None` | 110 | 120 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 94 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 120 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_LongSnap` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_None` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_None` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_None` | 40 | 52 | 13 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_None` | 87 | 120 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_BlockKick` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_None` | 62 | 120 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 41 | 38 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 120 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 36 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 40 | 37 | inferred_complete_timeline |
| `Action_None` | 43 | 71 | 29 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 120 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 22 | 19 | inferred_complete_timeline |
| `Action_None` | 36 | 49 | 14 | inferred_complete_timeline |
| `Action_None` | 58 | 77 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–29
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 29 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_None` | 49 | 120 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 120 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 16–120 | 54 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 42–120 | 36 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 45–66 | 8 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 49–120 | 72 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 59–120 | 50 | 6 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 70–74 | 5 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 104–120 | 14 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [4-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-29] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-120] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-22] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-49] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-22] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-36] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-52] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-85] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-22] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-34] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-120] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-120] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-120] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '27' has 2 frames without a visible bounding box.
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