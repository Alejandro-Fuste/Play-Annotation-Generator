# Play-Annotation-Generator Annotation Review — PuntBlock_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_80`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `25` | `23` |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | Team_Unknown | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 1 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `8` | `8` | 2 | START | 2 | 23 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 34 | END | 34 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `5` | `5` | 57 | START | 57 | 82 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Position_Unknown | `25` | `23` | 64 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureRecovery` | Position_Unknown | `20` | `20` | 228 | START | 228 | 233 |

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
- **Visible Frames:** 0–153
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 44 | 43 | inferred_complete_timeline |
| `Action_None` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 153 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 3 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 12 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 2 | 23 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 29 | 56 | 28 | inferred_complete_timeline |
| `Action_None` | 57 | 107 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 47 | 46 | inferred_complete_timeline |
| `Action_None` | 49 | 67 | 19 | inferred_complete_timeline |
| `Action_None` | 75 | 83 | 9 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 55 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 56 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 57 | 82 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 92 | 103 | 12 | inferred_complete_timeline |
| `Action_PuntBall` | 119 | 160 | 42 | inferred_complete_timeline |
| `Action_PuntBall` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_PuntBall` | 177 | 263 | 87 | inferred_complete_timeline |
| `Action_PuntBall` | 282 | 327 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 162 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 178 | 177 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 253 | 258 | 6 | inferred_complete_timeline |
| `Action_None` | 263 | 329 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 175 | 174 | inferred_complete_timeline |
| `Action_None` | 180 | 298 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 80 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 180 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 52 | 51 | inferred_complete_timeline |
| `Action_None` | 59 | 73 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 197 | 196 | inferred_complete_timeline |
| `Action_None` | 199 | 231 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 11 | 10 | inferred_complete_timeline |
| `Action_None` | 20 | 84 | 65 | inferred_complete_timeline |
| `Action_None` | 86 | 171 | 86 | inferred_complete_timeline |
| `Action_None` | 183 | 238 | 56 | inferred_complete_timeline |
| `Action_None` | 241 | 329 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 54 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 34 | 33 | inferred_complete_timeline |
| `Action_None` | 38 | 329 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 40 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 6–10 | 5 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 11–18 | 8 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 16–329 | 179 | 11 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 23–42 | 20 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 24–149 | 123 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 47–125 | 43 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 50–57 | 8 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 62–329 | 236 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 72–120 | 48 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 73–87 | 15 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 74–154 | 81 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 88–165 | 78 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 89–130 | 32 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 113–191 | 78 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 126–216 | 57 | 5 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 145–156 | 7 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 214–329 | 64 | 5 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 226–324 | 54 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 241–329 | 89 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 263–329 | 67 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 263–329 | 67 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 267–308 | 42 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 271–329 | 59 | 1 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 301–309 | 9 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 303–322 | 20 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `5` (6 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `25` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Wing` position mapped to `offense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 162: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [2-40] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [57-82] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [92-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [119-160] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [164-169] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [177-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [282-327] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [2-23] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-55] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-153] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-238] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-12] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-10] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-143] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [228-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-42] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-125] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-57] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-215] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-120] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-119] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-137] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-175] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-216] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-300] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-241] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-324] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-308] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-309] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-322] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>