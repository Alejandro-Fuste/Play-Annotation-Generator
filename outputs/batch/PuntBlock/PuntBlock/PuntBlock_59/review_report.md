# Play-Annotation-Generator Annotation Review — PuntBlock_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_59`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 72
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
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockPunt` | Long_Snapper | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 20 | START | 20 | 89 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 46 | END | 46 | 46 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 80 | START | 80 | 210 |
| ✅ EXACT | `Action_BlockPunt` | Long_Snapper | `13` | `13` | 90 | START | 90 | 97 |

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
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 59 | 40 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_None` | 71 | 73 | 3 | inferred_complete_timeline |
| `Action_None` | 75 | 183 | 109 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_LongSnap` | 20 | 89 | 70 | inferred_complete_timeline |
| `Action_BlockPunt` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 65 | 46 | inferred_complete_timeline |
| `Action_None` | 70 | 210 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_None` | 47 | 79 | 33 | inferred_complete_timeline |
| `Action_PuntBall` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 28 | 9 | inferred_complete_timeline |
| `Action_None` | 31 | 96 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 70 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 68–210 | 143 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 95–210 | 116 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 104–124 | 20 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 113–114 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 118–121 | 4 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 142–150 | 9 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 154–187 | 31 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 157–182 | 26 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 168–210 | 43 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 188–189 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 191–206 | 7 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 44 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [20-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [80-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-70] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-96] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-124] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-187] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-182] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '33' has 1 frames without a visible bounding box.
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

</details>