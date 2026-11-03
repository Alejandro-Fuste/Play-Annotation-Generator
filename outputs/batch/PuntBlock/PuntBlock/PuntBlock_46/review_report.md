# Play-Annotation-Generator Annotation Review — PuntBlock_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_46`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | defense | `7` | `7` |
| ⚠️ START CHANGED | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `34` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 21 | END | 21 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `8` | `8` | 47 | START | 47 | 57 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | `7` | `7` | 62 | START | 62 | 70 |
| ⚠️ START CHANGED | `Action_SecureRecovery` | Position_Unknown | `34` | `33` | 170 | START | 175 | 177 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–9
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 94 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 46 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_PuntBall` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_PuntBall` | 77 | 108 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 113 | 120 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 35 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 114 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 97 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_BlockPunt` | 62 | 70 | 9 | inferred_complete_timeline |
| `Action_None` | 71 | 101 | 31 | inferred_complete_timeline |
| `Action_None` | 103 | 147 | 45 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 129 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 209 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 104 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 80 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 3–39 | 37 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 12–210 | 199 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 14–94 | 72 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 36–210 | 172 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 46–122 | 77 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 49–107 | 46 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 53–134 | 82 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 61–94 | 34 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 75–135 | 61 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 76–77 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 79–210 | 132 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 92–135 | 43 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 106–152 | 47 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 119–126 | 8 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 140–158 | 16 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 160–210 | 51 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 172–197 | 9 | 2 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 174–187 | 14 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 175–190 | 16 | 2 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 178–210 | 31 | 2 | Undefined position; Undefined team |
| `35` | `36` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `8` (4 segments found)
- ⚠️ `Action_SecureRecovery` for actor_track_id `34` (Position_Unknown): Annotated start 170 != Inferred start 175

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 67 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-101] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-147] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [47-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [59-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [77-108] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [113-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-209] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-39] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-94] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-154] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-94] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-152] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-197] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-190] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-184] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-210] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>