# Play-Annotation-Generator Annotation Review — FieldGoalBlock_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_73`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `6` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_BlockKick` | Interior_Rusher2 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `10` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `5` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `6` | `6` | 16 | START | 16 | 28 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 40 | START | 40 | 44 |
| ⚠️ START CHANGED | `Action_BlockKick` | Interior_Rusher2 | `16` | `16` | 44 | START | 50 | 55 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PlaceBall` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 150 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_KickBall` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 150 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 108 | 69 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 57 | 18 | inferred_complete_timeline |
| `Action_None` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 66 | 27 | inferred_complete_timeline |
| `Action_None` | 74 | 99 | 26 | inferred_complete_timeline |
| `Action_None` | 101 | 107 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_None` | 40 | 68 | 29 | inferred_complete_timeline |
| `Action_None` | 73 | 76 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 80 | 41 | inferred_complete_timeline |
| `Action_None` | 92 | 150 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 55 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 116 | 77 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 86 | 43 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BlockKick` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 75 | 20 | inferred_complete_timeline |
| `Action_None` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_None` | 109 | 150 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_None` | 40 | 57 | 18 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 79 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 51 | 7 | inferred_complete_timeline |
| `Action_None` | 58 | 80 | 23 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_None` | 45 | 80 | 36 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_None` | 90 | 132 | 43 | inferred_complete_timeline |
| `Action_None` | 138 | 150 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_None` | 58 | 87 | 30 | inferred_complete_timeline |
| `Action_None` | 107 | 150 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 39 | 22 | inferred_complete_timeline |
| `Action_None` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_None` | 45 | 150 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 150 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_None` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 83 | 150 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 29–150 | 94 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 41–44 | 4 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 52–149 | 74 | 8 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 89–150 | 62 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 91–150 | 60 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 96–150 | 55 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 104–138 | 6 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 105–150 | 46 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 128–150 | 14 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockKick` for actor_track_id `16` (Interior_Rusher2): Annotated start 44 != Inferred start 50

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 84 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [40-66] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-99] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-56] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-132] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-150] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 40, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [40-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-39] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-57] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-79] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-87] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-108] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-86] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [50-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-75] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-37] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-85] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-150] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '27' has 1 frames without a visible bounding box.
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