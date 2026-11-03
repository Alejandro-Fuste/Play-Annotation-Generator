# Play-Annotation-Generator Annotation Review — PuntBlock_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_5`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `35` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `11` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `13` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `14` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `5` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `7` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `9` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 25 | END | 25 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `12` | `12` | 53 | START | 53 | 170 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `17` | `17` | 61 | START | 61 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Position_Unknown | `35` | `28` | 134 | START | 150 | 161 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_None` | 42 | 99 | 58 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 53 | 153 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 210 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 55 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_None` | 26 | 52 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 53 | 170 | 118 | inferred_complete_timeline |
| `Action_PuntBall` | 176 | 180 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 34 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 59 | 210 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_None` | 62 | 116 | 55 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_None` | 20 | 94 | 75 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 11 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 134 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 123 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 60 | 49 | inferred_complete_timeline |
| `Action_BlockPunt` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_None` | 68 | 92 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 5–210 | 206 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 9–210 | 202 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 54–165 | 112 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 89–96 | 8 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 98–210 | 109 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 103–210 | 108 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 110–135 | 17 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 150–210 | 60 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `35` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 51 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [0-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-57] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-210] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-123] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-210] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-141] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-23] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [53-170] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [176-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-34] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-210] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-203] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [150-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [163-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '30' has 1 frames without a visible bounding box.
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

</details>