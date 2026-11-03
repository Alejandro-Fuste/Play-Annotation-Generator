# Play-Annotation-Generator Annotation Review — PuntBlock_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Left_Wing | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Left_Wing | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_BlockPunt` | Interior_Rusher4 | defense | `5` | `5` |
| ⚠️ START CHANGED | `Action_SecureRecovery` | Interior_Rusher4 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `0` | `0` | 4 | START | 4 | 57 |
| ✅ EXACT | `Action_SnapReceive` | Left_Wing | `4` | `4` | 31 | END | 31 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Left_Wing | `4` | `4` | 58 | START | 58 | 92 |
| ⚠️ START CHANGED | `Action_BlockPunt` | Interior_Rusher4 | `5` | `5` | 67 | START | 72 | 72 |
| ⚠️ START CHANGED | `Action_SecureRecovery` | Interior_Rusher4 | `5` | `5` | 151 | START | 158 | 158 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 37 | 34 | inferred_complete_timeline |
| `Action_None` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_None` | 66 | 143 | 78 | inferred_complete_timeline |
| `Action_None` | 145 | 180 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_None` | 32 | 57 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 58 | 92 | 35 | inferred_complete_timeline |
| `Action_PuntBall` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_PuntBall` | 101 | 134 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_LongSnap` | 4 | 57 | 54 | inferred_complete_timeline |
| `Action_None` | 58 | 180 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 141 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 161 | 158 | inferred_complete_timeline |
| `Action_None` | 165 | 180 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 57 | 54 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 180 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 42 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 53 | 5 | inferred_complete_timeline |
| `Action_None` | 57 | 111 | 55 | inferred_complete_timeline |
| `Action_None` | 113 | 158 | 46 | inferred_complete_timeline |
| `Action_None` | 160 | 173 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 61 | 58 | inferred_complete_timeline |
| `Action_None` | 64 | 161 | 98 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 15 | 12 | inferred_complete_timeline |
| `Action_None` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_None` | 24 | 121 | 98 | inferred_complete_timeline |
| `Action_None` | 125 | 132 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 56–180
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 56 | 180 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 66 | 35 | inferred_complete_timeline |
| `Action_BlockPunt` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_None` | 73 | 131 | 59 | inferred_complete_timeline |
| `Action_SecureRecovery` | 158 | 158 | 1 | inferred_complete_timeline |
| `Action_None` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 136 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_None` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_None` | 23 | 25 | 3 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 173 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_None` | 17 | 36 | 20 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 61 | 58 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 105 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 7 | 4 | inferred_complete_timeline |
| `Action_None` | 14 | 64 | 51 | inferred_complete_timeline |
| `Action_None` | 69 | 139 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–155 | 146 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 60–105 | 42 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 82–180 | 90 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 91–109 | 19 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 108–180 | 22 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 116–161 | 46 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 120–180 | 58 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 125–129 | 5 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 129–171 | 43 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 133–142 | 10 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 138–150 | 13 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 146–149 | 4 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 149–153 | 5 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 155–164 | 10 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 156–180 | 25 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 175–180 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `4` (3 segments found)
- ⚠️ `Action_BlockPunt` for actor_track_id `5` (Interior_Rusher4): Annotated start 67 != Inferred start 72
- ⚠️ `Action_SecureRecovery` for actor_track_id `5` (Interior_Rusher4): Annotated start 151 != Inferred start 158

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 81 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [58-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-61] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-161] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [58-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [94-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [101-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-30] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-42] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-43] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-75] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-155] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-121] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-13] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-143] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-61] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-105] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-25] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-173] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-7] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-139] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-109] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>