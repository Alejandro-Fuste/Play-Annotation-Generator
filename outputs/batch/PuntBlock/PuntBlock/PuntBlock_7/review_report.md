# Play-Annotation-Generator Annotation Review — PuntBlock_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Right_Guard | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `25` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Right_Guard | `20` | `20` | 7 | START | 7 | 27 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 41 | END | 41 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `11` | `11` | 66 | START | 66 | 123 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `25` | `24` | 76 | START | 76 | 77 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 77 | 71 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 155 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 35 | 29 | inferred_complete_timeline |
| `Action_None` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_None` | 44 | 67 | 24 | inferred_complete_timeline |
| `Action_None` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 134 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 47 | 41 | inferred_complete_timeline |
| `Action_None` | 54 | 180 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 66 | 123 | 58 | inferred_complete_timeline |
| `Action_PuntBall` | 176 | 180 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 7 | 27 | 21 | inferred_complete_timeline |
| `Action_LongSnap` | 35 | 65 | 31 | inferred_complete_timeline |
| `Action_None` | 66 | 180 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 40 | 34 | inferred_complete_timeline |
| `Action_None` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 180 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_None` | 52 | 84 | 33 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 39 | 33 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 37 | 31 | inferred_complete_timeline |
| `Action_None` | 39 | 60 | 22 | inferred_complete_timeline |
| `Action_None` | 77 | 99 | 23 | inferred_complete_timeline |
| `Action_None` | 106 | 152 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 138 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 152 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–85 | 82 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 22–23 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 39–180 | 142 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 50–51 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 66–77 | 12 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 87–180 | 59 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 88–180 | 93 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 96–180 | 85 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 163–180 | 18 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 165–180 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 16: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [7-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-152] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-47] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-50] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [66-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [176-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-99] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-152] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-85] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-77] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [7-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [76-77] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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