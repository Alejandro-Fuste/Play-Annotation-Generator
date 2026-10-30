# Play-Annotation-Generator Annotation Review — FieldGoalBlock_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_74`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 109
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | Team_Unknown | `20` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `3` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 10 | START | 10 | 20 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 31 | START | 31 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | `20` | `19` | 37 | START | 37 | 40 |

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
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PlaceBall` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_None` | 21 | 106 | 86 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_KickBall` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_None` | 38 | 150 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 114 | 29 | inferred_complete_timeline |
| `Action_None` | 116 | 150 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 31 | 41 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 50 | 20 | inferred_complete_timeline |
| `Action_None` | 53 | 62 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 133 | 69 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 43 | 49 | 7 | inferred_complete_timeline |
| `Action_None` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_None` | 78 | 103 | 26 | inferred_complete_timeline |
| `Action_None` | 120 | 150 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 59 | 29 | inferred_complete_timeline |
| `Action_None` | 61 | 92 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 64 | 34 | inferred_complete_timeline |
| `Action_None` | 67 | 109 | 43 | inferred_complete_timeline |
| `Action_None` | 122 | 150 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 79 | 49 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 93 | 110 | 18 | inferred_complete_timeline |
| `Action_None` | 120 | 127 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 150 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 150 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 30 | 9 | inferred_complete_timeline |
| `Action_None` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_None` | 53 | 111 | 59 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 136 | 16 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 51 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 58 | 28 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 77 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 91 | 17 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 112 | 150 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 150 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–149 | 120 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 23–24 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 37–47 | 9 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 38–93 | 18 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 76–150 | 64 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 78–144 | 67 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 87–150 | 56 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 89–150 | 62 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 91–150 | 60 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 96–150 | 54 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 97–150 | 45 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 99–150 | 52 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 105–149 | 45 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 119–150 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 80 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-42] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-48] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-110] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-50] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [37-40] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [43-47] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-102] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-129] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-104] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-150] for track '30' has 1 frames without a visible bounding box.
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

</details>