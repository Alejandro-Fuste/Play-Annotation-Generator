# Play-Annotation-Generator Annotation Review — FieldGoalBlock_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_83`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockKick` | Left_Edge_Rusher | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `9` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 31 | START | 31 | 45 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 55 | START | 55 | 59 |
| ✅ EXACT | `Action_BlockKick` | Left_Edge_Rusher | `6` | `6` | 59 | START | 59 | 74 |

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
- **Visible Frames:** 0–152
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PlaceBall` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_None` | 70 | 140 | 71 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 152 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_KickBall` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_None` | 60 | 126 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 55 | 210 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 128 | 74 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_None` | 66 | 210 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 155 | 101 | inferred_complete_timeline |
| `Action_None` | 161 | 198 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 210 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 140 | 86 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 154 | 7 | inferred_complete_timeline |
| `Action_None` | 173 | 210 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 40 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–8
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 8 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BlockKick` | 59 | 74 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 210 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–92 | 80 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 8–210 | 176 | 7 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 15–210 | 185 | 4 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 21–167 | 98 | 5 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 23–117 | 91 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 53–210 | 132 | 8 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 59–210 | 127 | 10 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 71–183 | 89 | 9 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 82–103 | 22 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 89–210 | 111 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 106–210 | 73 | 5 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 108–210 | 92 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 112–138 | 27 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 95 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_KickBall' for track '0' starts at frame 55, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_KickBall' range [55-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [59-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-59] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 55, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [55-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-54] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-159] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-29] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-179] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-138] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>