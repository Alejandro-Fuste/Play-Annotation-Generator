# Play-Annotation-Generator Annotation Review — PuntBlock_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_51`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 1 | START | 1 | 20 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 30 | END | 30 | 30 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 62 | START | 62 | 92 |
| ✅ EXACT | `Action_BlockPunt` | Left_Edge_Rusher1 | `2` | `2` | 72 | START | 72 | 73 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `2` | `2` | 174 | START | N/A | N/A |

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
- **Visible Frames:** 0–39
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 23 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 39 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 32 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 43 | 43 | inferred_complete_timeline |
| `Action_None` | 50 | 180 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 20 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 47 | 47 | inferred_complete_timeline |
| `Action_None` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 32 | 32 | inferred_complete_timeline |
| `Action_None` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 53 | 53 | inferred_complete_timeline |
| `Action_None` | 61 | 68 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 61 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 62 | 92 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 66 | 66 | inferred_complete_timeline |
| `Action_None` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_None` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 165 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 43 | 180 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |
| `Action_None` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–9
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 9 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 61 | 61 | inferred_complete_timeline |
| `Action_None` | 63 | 67 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 26 | 26 | inferred_complete_timeline |
| `Action_None` | 39 | 68 | 30 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_None` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_None` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 66 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 71 | 13 | inferred_complete_timeline |
| `Action_BlockPunt` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 85 | 85 | inferred_complete_timeline |
| `Action_None` | 88 | 105 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 18–128 | 105 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 24–58 | 33 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 33–180 | 146 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 45–100 | 43 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 52–74 | 23 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 68–135 | 50 | 5 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 86–129 | 40 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 89–180 | 92 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 101–116 | 12 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 111–180 | 33 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 112–132 | 21 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 114–150 | 16 | 5 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 119–178 | 59 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 119–141 | 17 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 137–180 | 44 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 142–146 | 4 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 152–176 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureRecovery` on target `2` (Left_Edge_Rusher1)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '2' has invalid range: start=174, end=78. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-105] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-66] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [62-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-26] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [1-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-66] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-149] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-70] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-74] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-135] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-125] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-132] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-176] for track '36' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>