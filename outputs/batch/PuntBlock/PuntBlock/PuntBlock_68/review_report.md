# Play-Annotation-Generator Annotation Review — PuntBlock_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_68`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Right_Guard | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Right_Guard | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher6 | defense | `7` | `7` |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `3` | `3` | 16 | START | 16 | 45 |
| ✅ EXACT | `Action_SnapReceive` | Right_Guard | `11` | `11` | 41 | END | 41 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Right_Guard | `11` | `11` | 65 | START | 65 | 74 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher6 | `7` | `7` | 79 | START | 79 | 83 |
| ✅ EXACT | `Action_SecureRecovery` | Interior_Rusher1 | `2` | `2` | 192 | START | 192 | 204 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 77 | 62 | inferred_complete_timeline |
| `Action_None` | 81 | 116 | 36 | inferred_complete_timeline |
| `Action_None` | 123 | 138 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 45 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 47 | 64 | 18 | inferred_complete_timeline |
| `Action_None` | 65 | 91 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 239 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 68 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 98 | 83 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 121 | 106 | inferred_complete_timeline |
| `Action_None` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 64 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 65 | 74 | 10 | inferred_complete_timeline |
| `Action_PuntBall` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_PuntBall` | 93 | 269 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 37 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_SecureRecovery` | 192 | 204 | 13 | inferred_complete_timeline |
| `Action_None` | 205 | 228 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 42 | 27 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 89 | 100 | 12 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 178 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 136 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 37 | 57 | 21 | inferred_complete_timeline |
| `Action_None` | 108 | 123 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BlockPunt` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_None` | 84 | 161 | 78 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 55 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 125 | 110 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–151 | 99 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 40–269 | 216 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 50–269 | 219 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 57–86 | 20 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 62–267 | 206 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 91–120 | 28 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 115–216 | 100 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 117–148 | 32 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 123–164 | 30 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 136–142 | 7 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 147–148 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 151–233 | 82 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 152–259 | 108 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 164–215 | 52 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 194–269 | 74 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 201–220 | 20 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 205–215 | 11 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 232–243 | 12 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 244–269 | 26 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 69 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-55] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-121] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [192-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [16-45] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-57] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [65-74] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [77-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [93-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-136] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-4] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-23] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-267] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-120] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-215] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-215] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-243] for track '33' has 1 frames without a visible bounding box.
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