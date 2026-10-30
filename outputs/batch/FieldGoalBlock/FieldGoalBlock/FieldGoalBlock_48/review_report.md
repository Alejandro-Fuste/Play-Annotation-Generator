# Play-Annotation-Generator Annotation Review — FieldGoalBlock_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_48`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `20` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 11 | START | 11 | 25 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `12` | `12` | 26 | START | 26 | 41 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 47 | START | 47 | 51 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `20` | `18` | 51 | START | 51 | 58 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PlaceBall` | 26 | 41 | 16 | inferred_complete_timeline |
| `Action_None` | 42 | 131 | 90 | inferred_complete_timeline |
| `Action_None` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 127 | 34 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 48 | 38 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 55 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 59 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 34 | 9 | inferred_complete_timeline |
| `Action_None` | 38 | 44 | 7 | inferred_complete_timeline |
| `Action_None` | 46 | 58 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 32 | 22 | inferred_complete_timeline |
| `Action_None` | 36 | 91 | 56 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 27 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 48 | 20 | inferred_complete_timeline |
| `Action_None` | 51 | 78 | 28 | inferred_complete_timeline |
| `Action_None` | 82 | 95 | 14 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 150 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 90 | 80 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 130 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 137 | 127 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 93 | 83 | inferred_complete_timeline |
| `Action_None` | 115 | 131 | 17 | inferred_complete_timeline |
| `Action_None` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 40 | 30 | inferred_complete_timeline |
| `Action_None` | 61 | 150 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 35 | 25 | inferred_complete_timeline |
| `Action_None` | 40 | 42 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 78 | 68 | inferred_complete_timeline |
| `Action_None` | 80 | 89 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 36 | 26 | inferred_complete_timeline |
| `Action_None` | 38 | 150 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 81 | 71 | inferred_complete_timeline |
| `Action_None` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 101 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 21–32 | 12 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 24–150 | 108 | 5 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 41–149 | 99 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 53–68 | 14 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 56–89 | 14 | 6 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 62–147 | 44 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 67–89 | 15 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 95–150 | 56 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 109–112 | 4 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 114–150 | 37 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 121–123 | 3 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 123–146 | 23 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 128–150 | 23 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 79 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [11-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-127] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-131] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-150] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-130] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-91] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-150] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-131] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-59] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-48] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-101] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-142] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-80] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-100] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '31' has 1 frames without a visible bounding box.
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

</details>