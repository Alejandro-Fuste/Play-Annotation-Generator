# Play-Annotation-Generator Annotation Review — PuntBlock_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_34`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 121
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
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockPunt` | Punt_Support3 | defense | `9` | `9` |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | defense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 14 | START | 14 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 41 | END | 41 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `8` | `8` | 67 | START | 67 | 104 |
| ✅ EXACT | `Action_BlockPunt` | Punt_Support3 | `9` | `9` | 81 | START | 81 | 84 |
| ✅ EXACT | `Action_SecureRecovery` | Left_Edge_Rusher1 | `12` | `12` | 137 | START | 137 | 151 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 208 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 104 | 91 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LongSnap` | 14 | 66 | 53 | inferred_complete_timeline |
| `Action_None` | 67 | 104 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 102 | 89 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 109 | 223 | 115 | inferred_complete_timeline |
| `Action_None` | 232 | 268 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 136 | 123 | inferred_complete_timeline |
| `Action_None` | 140 | 181 | 42 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 241 | 255 | 15 | inferred_complete_timeline |
| `Action_None` | 257 | 267 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 103 | 90 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 136 | 28 | inferred_complete_timeline |
| `Action_None` | 140 | 194 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 66 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 104 | 38 | inferred_complete_timeline |
| `Action_PuntBall` | 113 | 130 | 18 | inferred_complete_timeline |
| `Action_PuntBall` | 144 | 221 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 269 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 74 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 20 | 7 | inferred_complete_timeline |
| `Action_None` | 22 | 28 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 57 | 44 | inferred_complete_timeline |
| `Action_None` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 199 | 129 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 18 | 5 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_None` | 27 | 67 | 41 | inferred_complete_timeline |
| `Action_None` | 69 | 141 | 73 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 199 | 46 | inferred_complete_timeline |
| `Action_None` | 203 | 208 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 266 | 57 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_SecureRecovery` | 137 | 151 | 15 | inferred_complete_timeline |
| `Action_None` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 201 | 23 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 29 | 16 | inferred_complete_timeline |
| `Action_None` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_None` | 40 | 71 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BlockPunt` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 136 | 123 | inferred_complete_timeline |
| `Action_None` | 145 | 160 | 16 | inferred_complete_timeline |
| `Action_None` | 162 | 192 | 31 | inferred_complete_timeline |
| `Action_None` | 208 | 217 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 3–204 | 186 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 51–64 | 14 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 74–92 | 17 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 81–150 | 70 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 88–223 | 130 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 91–269 | 58 | 7 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 110–223 | 107 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 114–125 | 12 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 126–269 | 111 | 4 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 222–269 | 41 | 2 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 236–268 | 33 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 250–269 | 19 | 2 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 85 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [14-74] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-136] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-181] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-255] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-102] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-268] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-104] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-194] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-104] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [113-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [144-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-57] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-136] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-28] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-67] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-266] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-178] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '31' has 1 frames without a visible bounding box.
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

</details>