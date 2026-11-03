# Play-Annotation-Generator Annotation Review — PuntBlock_14

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 60
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 4 | START | 4 | 54 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 30 | END | 30 | 30 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 55 | START | 55 | 80 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | `16` | `16` | 64 | START | 64 | 70 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 130 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 94 | 91 | inferred_complete_timeline |
| `Action_None` | 98 | 150 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_LongSnap` | 4 | 54 | 51 | inferred_complete_timeline |
| `Action_None` | 55 | 141 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 76 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 47 | 44 | inferred_complete_timeline |
| `Action_None` | 57 | 62 | 6 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 150 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 38 | 54 | 17 | inferred_complete_timeline |
| `Action_PuntBall` | 55 | 80 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 31 | 28 | inferred_complete_timeline |
| `Action_None` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_None` | 76 | 103 | 28 | inferred_complete_timeline |
| `Action_None` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 135 | 132 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 125 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 76 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 107 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_None` | 31 | 123 | 93 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 63 | 24 | inferred_complete_timeline |
| `Action_BlockPunt` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 71 | 81 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 59 | 56 | inferred_complete_timeline |
| `Action_None` | 61 | 150 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 147 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 121 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `23` | Position_Unknown | Team_Unknown | 73–130 | 54 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 79–150 | 72 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 87–150 | 61 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 91–150 | 59 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SecureRecovery' at frame 123 targets track ID '120', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 48 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [4-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-94] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [55-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-76] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-125] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-29] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-31] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-47] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-103] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 4, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [4-47] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-150] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-101] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '23' has 1 frames without a visible bounding box.
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

</details>