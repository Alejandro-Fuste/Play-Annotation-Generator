# Play-Annotation-Generator Annotation Review — PuntBlock_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_8`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Interior_Rusher2 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `14` | `14` | 15 | START | 15 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 42 | END | 42 | 42 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 67 | START | 67 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Interior_Rusher2 | `6` | `6` | 77 | START | 77 | 80 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 99 | 85 | inferred_complete_timeline |
| `Action_None` | 102 | 142 | 41 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 58 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 65 | 51 | inferred_complete_timeline |
| `Action_None` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 58 | 44 | inferred_complete_timeline |
| `Action_None` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 210 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 100 | 86 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 129 | 23 | inferred_complete_timeline |
| `Action_None` | 140 | 210 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 66 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 95 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_LongSnap` | 15 | 66 | 52 | inferred_complete_timeline |
| `Action_None` | 67 | 210 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 85 | 71 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 100 | 129 | 30 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BlockPunt` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_BlockPunt` | 82 | 82 | 1 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 31 | 17 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 210 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 106 | 92 | inferred_complete_timeline |
| `Action_None` | 108 | 210 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 83 | 69 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–86 | 76 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 68–210 | 143 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 78–107 | 23 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 91–97 | 6 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 91–210 | 113 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 108–190 | 83 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 111–210 | 98 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 112–210 | 97 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 113–190 | 78 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 120–210 | 91 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 124–132 | 9 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 150–210 | 61 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 186–192 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 18: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [15-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [77-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-193] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-190] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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