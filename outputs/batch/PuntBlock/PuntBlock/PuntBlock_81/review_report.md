# Play-Annotation-Generator Annotation Review — PuntBlock_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Personal_Protector3 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `29` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_LongSnap` | Personal_Protector3 | `7` | `7` | 12 | START | 12 | 64 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 39 | END | 39 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `3` | `3` | 65 | START | 65 | 104 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Position_Unknown | `29` | `21` | 76 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Gunner — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 136 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 11 | 3 | inferred_complete_timeline |
| `Action_None` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_None` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 239 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 52 | 41 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_LongSnap` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 112 | 43 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 219 | 67 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_None` | 40 | 64 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 65 | 104 | 40 | inferred_complete_timeline |
| `Action_PuntBall` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PuntBall` | 123 | 155 | 33 | inferred_complete_timeline |
| `Action_PuntBall` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_PuntBall` | 171 | 175 | 5 | inferred_complete_timeline |
| `Action_PuntBall` | 182 | 193 | 12 | inferred_complete_timeline |
| `Action_PuntBall` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_None` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_None` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 124 | 167 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 131 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 239 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 61 | 50 | inferred_complete_timeline |
| `Action_None` | 67 | 239 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 11 | 3 | inferred_complete_timeline |
| `Action_None` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_None` | 29 | 34 | 6 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 21 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 61 | 38 | inferred_complete_timeline |
| `Action_None` | 64 | 239 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 108 | 97 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 229 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 84 | 143 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 17–219 | 203 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 19–239 | 196 | 3 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 25–139 | 102 | 5 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 30–239 | 193 | 4 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 49–70 | 22 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 65–97 | 17 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 86–96 | 10 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 105–239 | 130 | 4 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 120–239 | 99 | 5 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 144–239 | 71 | 10 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 166–239 | 9 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `3` (7 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `29` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 79 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [12-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [65-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [107-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [123-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [161-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [171-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [182-193] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [12-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-219] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-75] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-61] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-21] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-79] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-21] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-34] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-21] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-42] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-219] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-203] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-139] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-176] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-212] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-187] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-199] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '26' has 1 frames without a visible bounding box.
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

</details>