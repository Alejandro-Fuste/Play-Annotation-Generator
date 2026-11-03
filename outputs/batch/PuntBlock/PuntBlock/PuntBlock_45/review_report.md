# Play-Annotation-Generator Annotation Review — PuntBlock_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_45`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 96
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockPunt` | Punt_Support1 | defense | `2` | `2` |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher4 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `0` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 13 | START | 13 | 67 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 38 | END | 38 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `8` | `8` | 71 | START | 71 | 95 |
| ✅ EXACT | `Action_BlockPunt` | Punt_Support1 | `2` | `2` | 84 | START | 84 | 87 |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher4 | `6` | `6` | 191 | START | 191 | 191 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 77 | 65 | inferred_complete_timeline |
| `Action_None` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_None` | 103 | 116 | 14 | inferred_complete_timeline |
| `Action_None` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 165 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 192 | 180 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_LongSnap` | 13 | 67 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 73 | 61 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 63 | 51 | inferred_complete_timeline |
| `Action_None` | 66 | 73 | 8 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 70 | 58 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 158 | 77 | inferred_complete_timeline |
| `Action_None` | 160 | 210 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 70 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 71 | 95 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 41 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 164 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 111 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 192 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 97 | 85 | inferred_complete_timeline |
| `Action_None` | 101 | 171 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 33 | 21 | inferred_complete_timeline |
| `Action_None` | 40 | 195 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 163 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 190 | 23 | inferred_complete_timeline |
| `Action_SecureRecovery` | 191 | 191 | 1 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 54 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 47 | 35 | inferred_complete_timeline |
| `Action_None` | 49 | 65 | 17 | inferred_complete_timeline |
| `Action_None` | 69 | 171 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 61 | 49 | inferred_complete_timeline |
| `Action_None` | 63 | 190 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_BlockPunt` | 84 | 87 | 4 | inferred_complete_timeline |
| `Action_None` | 88 | 204 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 109 | 97 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 127 | 135 | 9 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 96 | 84 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 168 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 43–210 | 168 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 84–174 | 89 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 95–177 | 83 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 104–177 | 14 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 110–210 | 90 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 117–163 | 47 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 133–168 | 32 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 181–210 | 24 | 4 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 198–206 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 72 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [13-111] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' for track '2' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockPunt' range [84-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-204] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-99] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-116] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' for track '6' starts at frame 191, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SecureRecovery' range [191-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-47] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-65] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-171] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [71-95] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [97-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-96] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [13-67] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-192] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-165] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-190] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-33] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-111] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-168] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '31' has 1 frames without a visible bounding box.
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