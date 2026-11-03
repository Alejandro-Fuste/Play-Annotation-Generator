# Play-Annotation-Generator Annotation Review — PuntBlock_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_64`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Interior_Rusher4 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Interior_Rusher4 | defense | `11` | `11` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | defense | `10` | `10` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `16` | `16` | 28 | START | 28 | 77 |
| ✅ EXACT | `Action_SnapReceive` | Interior_Rusher4 | `11` | `11` | 53 | END | 53 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Interior_Rusher4 | `11` | `11` | 78 | START | 78 | 107 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher2 | `10` | `10` | 86 | START | 86 | 101 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `2` | `2` | 174 | START | 174 | 182 |

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
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 46 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 160 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 154 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_LongSnap` | 28 | 77 | 50 | inferred_complete_timeline |
| `Action_None` | 78 | 148 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 72 | 45 | inferred_complete_timeline |
| `Action_None` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 74 | 47 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 105 | 78 | inferred_complete_timeline |
| `Action_None` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 103 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 167 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BlockPunt` | 86 | 101 | 16 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_None` | 54 | 77 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 78 | 107 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 84 | 57 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_SecureRecovery` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 204 | 22 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 210 | 183 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 57–203 | 135 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 66–143 | 78 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 83–144 | 62 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 100–210 | 111 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 105–210 | 105 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 118–210 | 68 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 40 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [28-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-105] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-204] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-103] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [78-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [114-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-149] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '22' has 1 frames without a visible bounding box.
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