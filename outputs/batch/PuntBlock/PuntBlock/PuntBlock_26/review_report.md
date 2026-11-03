# Play-Annotation-Generator Annotation Review — PuntBlock_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_26`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | defense | `13` | `13` |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `26` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `17` | `17` | 1 | START | 1 | 51 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 28 | END | 28 | 28 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 52 | START | 52 | 180 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | `13` | `13` | 64 | START | 64 | 71 |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | `26` | `24` | 148 | START | 148 | 154 |

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
- **Visible Frames:** 0–53
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 45 | 45 | inferred_complete_timeline |
| `Action_None` | 48 | 53 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 55 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 163 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 49 | 49 | inferred_complete_timeline |
| `Action_None` | 54 | 210 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 62 | 62 | inferred_complete_timeline |
| `Action_None` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 53 | 53 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_None` | 29 | 51 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 52 | 180 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 51 | 51 | inferred_complete_timeline |
| `Action_None` | 52 | 148 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 112 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 19 | 19 | inferred_complete_timeline |
| `Action_None` | 25 | 98 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 141 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 109 | 109 | inferred_complete_timeline |
| `Action_None` | 111 | 194 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 55 | 55 | inferred_complete_timeline |
| `Action_None` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BlockPunt` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 117 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 133 | 133 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 141 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 67 | 67 | inferred_complete_timeline |
| `Action_None` | 80 | 159 | 80 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 17–24 | 8 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 56–141 | 86 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 70–210 | 136 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 84–181 | 98 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 90–148 | 59 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 206–209 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 42 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [1-45] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-62] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-55] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [52-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-109] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-133] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '29' has 1 frames without a visible bounding box.
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

</details>