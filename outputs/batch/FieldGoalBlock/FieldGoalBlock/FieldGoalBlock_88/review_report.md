# Play-Annotation-Generator Annotation Review — FieldGoalBlock_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_88`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `4` | `4` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `19` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `14` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `16` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `4` | `4` | 20 | START | 20 | 37 |
| ✅ EXACT | `Action_KickBall` | Kicker | `3` | `3` | 47 | START | 47 | 51 |
| ❌ MISSING SEGMENT | `Action_BlockKick` | Position_Unknown | `19` | `18` | 81 | START | N/A | N/A |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PlaceBall` | 20 | 37 | 18 | inferred_complete_timeline |
| `Action_None` | 38 | 180 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 47 | 51 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 85 | 34 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 150 | 24 | inferred_complete_timeline |
| `Action_None` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_None` | 53 | 104 | 52 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 156 | 29 | inferred_complete_timeline |
| `Action_None` | 160 | 180 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 80 | 34 | inferred_complete_timeline |
| `Action_None` | 86 | 107 | 22 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 90 | 44 | inferred_complete_timeline |
| `Action_None` | 93 | 175 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 47 | 57 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_None` | 68 | 180 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_None` | 63 | 90 | 28 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |
| `Action_None` | 113 | 126 | 14 | inferred_complete_timeline |
| `Action_None` | 133 | 143 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 53 | 78 | 26 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_None` | 95 | 135 | 41 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_None` | 47 | 47 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 46 | 26 | inferred_complete_timeline |
| `Action_None` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 134 | 10 | inferred_complete_timeline |
| `Action_None` | 149 | 163 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_None` | 47 | 165 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_None` | 65 | 83 | 19 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_None` | 61 | 93 | 33 | inferred_complete_timeline |
| `Action_None` | 95 | 143 | 49 | inferred_complete_timeline |
| `Action_None` | 150 | 154 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–18 | 19 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 4–180 | 29 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 11–32 | 17 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 16–44 | 19 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 46–75 | 25 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 46–170 | 74 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 46–180 | 108 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 87–133 | 42 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 90–104 | 10 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 96–180 | 25 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 113–118 | 6 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 117–180 | 64 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 122–180 | 39 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 129–153 | 25 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 149–180 | 28 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 162–180 | 17 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BlockKick` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Wing` position mapped to `offense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 116 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [47-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-107] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-57] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-90] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-126] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-65] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-78] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-165] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 47, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [47-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-57] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-40] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 47, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [47-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '23' starts at frame 47, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [47-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-127] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-153] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>