# Play-Annotation-Generator Annotation Review — PuntBlock_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_74`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 125
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher6 | defense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Punter | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 16 | START | 16 | 70 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 41 | END | 41 | 41 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 71 | START | 71 | 138 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher6 | `10` | `10` | 82 | START | 82 | 86 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Punter | `2` | `2` | 181 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 119 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 141 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 329 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 70 | 55 | inferred_complete_timeline |
| `Action_None` | 71 | 119 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 94 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 192 | 177 | inferred_complete_timeline |
| `Action_None` | 244 | 248 | 5 | inferred_complete_timeline |
| `Action_None` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_None` | 262 | 313 | 52 | inferred_complete_timeline |
| `Action_None` | 315 | 320 | 6 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 70 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 71 | 138 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 103 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 208 | 193 | inferred_complete_timeline |
| `Action_None` | 214 | 260 | 47 | inferred_complete_timeline |
| `Action_None` | 262 | 280 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 166 | 151 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 138 | 123 | inferred_complete_timeline |
| `Action_None` | 142 | 214 | 73 | inferred_complete_timeline |
| `Action_None` | 286 | 289 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 255 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 152 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_None` | 58 | 63 | 6 | inferred_complete_timeline |
| `Action_None` | 67 | 138 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BlockPunt` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_None` | 87 | 175 | 89 | inferred_complete_timeline |
| `Action_None` | 230 | 323 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 173 | 158 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_None` | 183 | 329 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 274 | 259 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 60–63 | 4 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 69–118 | 47 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 73–129 | 57 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 99–110 | 12 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 101–119 | 19 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 108–127 | 20 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 109–230 | 113 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 111–121 | 11 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 130–131 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 161–183 | 20 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 165–329 | 160 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 177–316 | 138 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 181–329 | 141 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 184–310 | 37 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 197–201 | 5 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 205–245 | 35 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 221–329 | 105 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 221–329 | 109 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 244–329 | 85 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 281–329 | 40 | 3 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 303–305 | 3 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureRecovery` on target `2` (Punter)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '2' has invalid range: start=181, end=138. Clamping end to start.
- ⚠️ Action 'Action_None' range [16-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [71-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-260] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-313] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-103] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-274] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-323] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-255] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-63] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-173] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-230] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-228] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-316] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-310] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-323] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '41' has 1 frames without a visible bounding box.
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

</details>