# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_21`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `1` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `3` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `6` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `9` | `Group` | 0 | START | 0 | 168 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `7` | `7` | 169 | START | 169 | 221 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 197 | END | 197 | 197 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 222 | START | 222 | 231 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 449 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 449 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 449 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_LongSnap` | 169 | 221 | 53 | inferred_complete_timeline |
| `Action_None` | 222 | 313 | 92 | inferred_complete_timeline |
| `Action_None` | 317 | 449 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 241 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 449 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 209 | 41 | inferred_complete_timeline |
| `Action_None` | 224 | 229 | 6 | inferred_complete_timeline |
| `Action_None` | 241 | 257 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_SnapReceive` | 197 | 197 | 1 | inferred_complete_timeline |
| `Action_None` | 198 | 221 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 222 | 231 | 10 | inferred_complete_timeline |
| `Action_None` | 232 | 449 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 449 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 237 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 285 | 117 | inferred_complete_timeline |
| `Action_None` | 290 | 449 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 267 | 99 | inferred_complete_timeline |
| `Action_None` | 279 | 449 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 209 | 41 | inferred_complete_timeline |
| `Action_None` | 213 | 449 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 186 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_None` | 177 | 189 | 13 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 168 | 154 | inferred_complete_timeline |
| `Action_None` | 169 | 449 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 79 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 304 | 136 | inferred_complete_timeline |
| `Action_None` | 306 | 309 | 4 | inferred_complete_timeline |
| `Action_None` | 311 | 449 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 215 | 47 | inferred_complete_timeline |
| `Action_None` | 223 | 449 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–421
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_None` | 169 | 235 | 67 | inferred_complete_timeline |
| `Action_None` | 237 | 376 | 140 | inferred_complete_timeline |
| `Action_None` | 378 | 404 | 27 | inferred_complete_timeline |
| `Action_None` | 417 | 418 | 2 | inferred_complete_timeline |
| `Action_None` | 420 | 421 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 19–308 | 270 | 7 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 70–449 | 374 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 136–181 | 28 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 201–449 | 243 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 207–296 | 90 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 238–449 | 212 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 239–449 | 197 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 251–443 | 193 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 281–287 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 287–294 | 8 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 312–315 | 4 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 317–378 | 62 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 56 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [169-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-376] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-404] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [169-221] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-313] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-186] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-449] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-285] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-449] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-168] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-449] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-137] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-195] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-308] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-149] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-163] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-250] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-449] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-296] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-309] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-443] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-378] for track '31' has 2 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>