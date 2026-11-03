# Play-Annotation-Generator Annotation Review — PuntBlock_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 117
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
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockPunt` | Right_Guard | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Guard | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `18` | `18` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `1` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `3` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `7` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 24 | END | 24 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `10` | `10` | 47 | START | 47 | 71 |
| ✅ EXACT | `Action_BlockPunt` | Right_Guard | `12` | `12` | 59 | START | 59 | 67 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Guard | `12` | `12` | 113 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 21 | 176 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_None` | 47 | 86 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 12 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_LongSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 128 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 33 | 41 | 9 | inferred_complete_timeline |
| `Action_None` | 50 | 105 | 56 | inferred_complete_timeline |
| `Action_None` | 110 | 144 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_None` | 66 | 77 | 12 | inferred_complete_timeline |
| `Action_None` | 79 | 180 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 25 | 46 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 47 | 71 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BlockPunt` | 59 | 67 | 9 | inferred_complete_timeline |
| `Action_None` | 68 | 92 | 25 | inferred_complete_timeline |
| `Action_None` | 100 | 108 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_None` | 86 | 105 | 20 | inferred_complete_timeline |
| `Action_None` | 114 | 149 | 36 | inferred_complete_timeline |
| `Action_None` | 151 | 158 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 38 | 97 | 60 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 42 | 60 | 19 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 180 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 51 | 77 | 27 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 116 | 10 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 141 | 180 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 33 | 37 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_None` | 37 | 119 | 83 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 0 | 89 | 90 | inferred_complete_timeline |

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
| `Action_None` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–59 | 58 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–180 | 165 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 3–6 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 17–180 | 164 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 17–105 | 89 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 29–99 | 70 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 39–67 | 29 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 50–180 | 128 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 63–180 | 115 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 88–123 | 34 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 143–180 | 31 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 174–180 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `12` (Right_Guard)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 28: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '12' has invalid range: start=113, end=108. Clamping end to start.
- ⚠️ Action 'Action_None' range [0-20] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-27] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-105] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-40] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-60] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-52] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-77] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-29] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-37] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-27] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [47-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [73-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-92] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-119] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-101] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-49] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [0-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-36] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-97] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [0-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-75] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-6] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-77] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-99] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-67] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-66] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-116] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-180] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-123] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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