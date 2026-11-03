# Play-Annotation-Generator Annotation Review — PuntBlock_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_63`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_BlockPunt` | Long_Snapper | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 1 | START | 1 | 57 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 27 | END | 27 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `14` | `14` | 52 | START | 52 | 68 |
| ✅ EXACT | `Action_BlockPunt` | Long_Snapper | `11` | `11` | 58 | START | 58 | 71 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `8` | `8` | 144 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 22 | 22 | inferred_complete_timeline |
| `Action_None` | 26 | 55 | 30 | inferred_complete_timeline |
| `Action_None` | 60 | 197 | 138 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 102 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 18 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 119 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 57 | 57 | inferred_complete_timeline |
| `Action_BlockPunt` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 72 | 105 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 51 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 175 | 106 | inferred_complete_timeline |
| `Action_PuntBall` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 79 | 79 | inferred_complete_timeline |
| `Action_None` | 82 | 179 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 100 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 129 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 113 | 113 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 19 | 19 | inferred_complete_timeline |
| `Action_None` | 21 | 29 | 9 | inferred_complete_timeline |
| `Action_None` | 36 | 115 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 162 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 40 | 40 | inferred_complete_timeline |
| `Action_None` | 46 | 52 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 187 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 101 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 102 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–55 | 53 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 48–178 | 131 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 62–162 | 101 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–239 | 167 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 81–86 | 6 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 106–141 | 29 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 120–162 | 43 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 124–133 | 10 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 183–227 | 42 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 186–223 | 38 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 202–238 | 37 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 203–217 | 12 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 213–239 | 23 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 214–224 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `14` (3 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `8` (Left_Edge_Rusher1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 128: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '8' has invalid range: start=144, end=137. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-52] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-162] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [52-68] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [70-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-113] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-48] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-19] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-162] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-239] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-134] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>