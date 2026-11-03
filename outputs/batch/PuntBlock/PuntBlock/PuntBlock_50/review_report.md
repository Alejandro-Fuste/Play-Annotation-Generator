# Play-Annotation-Generator Annotation Review — PuntBlock_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_50`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 48
- **Validation Warnings:** 45
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 34
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockPunt` | Personal_Protector2 | offense | `4` | `4` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_LongSnap` | Left_Guard | `0` | `0` | 14 | START | 14 | 91 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 43 | END | 43 | 43 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 92 | START | 92 | 180 |
| ✅ EXACT | `Action_BlockPunt` | Personal_Protector2 | `4` | `4` | 101 | START | 101 | 109 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `14` | `14` | 180 | START | 180 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LongSnap` | 14 | 91 | 78 | inferred_complete_timeline |
| `Action_None` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 172 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BlockPunt` | 101 | 109 | 9 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 124 | 10 | inferred_complete_timeline |
| `Action_None` | 126 | 180 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_None` | 44 | 91 | 48 | inferred_complete_timeline |
| `Action_PuntBall` | 92 | 180 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 40 | 27 | inferred_complete_timeline |
| `Action_None` | 46 | 58 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_SecureRecovery` | 180 | 180 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 67 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 37–152 | 116 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 46–180 | 135 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 57–98 | 42 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 74–180 | 107 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 99–180 | 79 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 118–140 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 29 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [92-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [92-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' for track '14' starts at frame 180, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SecureRecovery' range [180-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-152] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-98] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '22' has 1 frames without a visible bounding box.
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

</details>