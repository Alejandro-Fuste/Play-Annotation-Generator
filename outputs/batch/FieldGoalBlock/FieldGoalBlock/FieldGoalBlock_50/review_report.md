# Play-Annotation-Generator Annotation Review — FieldGoalBlock_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_50`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 97
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
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `15` | `15` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockKick` | Left_End2 | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End2 | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `4` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End1 | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `15` | `15` | 18 | START | 18 | 33 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `8` | `8` | 34 | START | 34 | 46 |
| ✅ EXACT | `Action_KickBall` | Kicker | `4` | `4` | 59 | START | 59 | 63 |
| ✅ EXACT | `Action_BlockKick` | Left_End2 | `12` | `12` | 63 | START | 63 | 72 |

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
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PlaceBall` | 34 | 46 | 13 | inferred_complete_timeline |
| `Action_None` | 47 | 150 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_KickBall` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 150 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 61 | 44 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_BlockKick` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 69 | 52 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 59 | 42 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 60 | 43 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_None` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 43 | 61 | 19 | inferred_complete_timeline |
| `Action_None` | 66 | 78 | 13 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 133 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 119 | 102 | inferred_complete_timeline |
| `Action_None` | 121 | 148 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 99 | 82 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 129 | 19 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 95 | 26 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 45 | 28 | inferred_complete_timeline |
| `Action_None` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_None` | 69 | 150 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 17 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 18 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 20 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 28 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 48 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 17–150 | 59 | 8 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 29–150 | 92 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 71–84 | 14 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 79–129 | 49 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 87–150 | 58 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 90–105 | 15 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 102–148 | 47 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 102–147 | 46 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 106–147 | 24 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 119–150 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_End1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_End2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 76 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [18-45] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-95] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-148] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-133] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-48] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [63-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-69] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-59] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 18, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [18-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-37] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-109] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-129] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-137] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-105] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-148] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-150] for track '28' has 1 frames without a visible bounding box.
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

</details>