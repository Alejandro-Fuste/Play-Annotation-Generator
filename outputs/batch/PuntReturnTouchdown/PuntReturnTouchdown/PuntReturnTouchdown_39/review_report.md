# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_39`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 151
- **Validation Warnings:** 196
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 140
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `16` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 179 |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | `3` | `3` | 180 | START | 180 | 232 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 209 | END | 209 | 209 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 233 | START | 233 | 241 |

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
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 329 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 341 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–447
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 246 | 67 | inferred_complete_timeline |
| `Action_None` | 248 | 267 | 20 | inferred_complete_timeline |
| `Action_None` | 273 | 279 | 7 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 290 | 439 | 150 | inferred_complete_timeline |
| `Action_None` | 442 | 447 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 195 | 16 | inferred_complete_timeline |
| `Action_None` | 222 | 253 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 228 | 49 | inferred_complete_timeline |
| `Action_None` | 237 | 244 | 8 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_SnapReceive` | 209 | 209 | 1 | inferred_complete_timeline |
| `Action_None` | 210 | 232 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 233 | 241 | 9 | inferred_complete_timeline |
| `Action_None` | 242 | 298 | 57 | inferred_complete_timeline |
| `Action_None` | 301 | 449 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 206 | 27 | inferred_complete_timeline |
| `Action_None` | 212 | 279 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 212 | 33 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 291 | 112 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_None` | 205 | 422 | 218 | inferred_complete_timeline |
| `Action_None` | 432 | 449 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 195 | 16 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 198 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 219 | 40 | inferred_complete_timeline |
| `Action_None` | 222 | 334 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 199 | 20 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 250 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 279 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 321 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–335 | 336 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–319 | 319 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–320 | 281 | 15 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 4–276 | 254 | 7 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 4–72 | 7 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 139–190 | 31 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 180–205 | 24 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 201–428 | 210 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 208–252 | 33 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 214–230 | 17 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 229–271 | 41 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 231–354 | 114 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 240–314 | 25 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 250–251 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 262–264 | 3 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 267–275 | 9 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 275–322 | 26 | 3 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 291–327 | 8 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 294–404 | 102 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 303–332 | 30 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 305–309 | 4 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 307–449 | 139 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 307–308 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 309–425 | 116 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 318–449 | 131 | 2 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 318–324 | 7 | 1 | Undefined position; Undefined team |
| `42` | `68` | Position_Unknown | Team_Unknown | 331–449 | 110 | 4 | Undefined position; Undefined team |
| `43` | `69` | Position_Unknown | Team_Unknown | 331–431 | 91 | 4 | Undefined position; Undefined team |
| `44` | `71` | Position_Unknown | Team_Unknown | 342–387 | 43 | 2 | Undefined position; Undefined team |
| `45` | `74` | Position_Unknown | Team_Unknown | 344–449 | 96 | 4 | Undefined position; Undefined team |
| `46` | `75` | Position_Unknown | Team_Unknown | 345–364 | 20 | 1 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 366–449 | 84 | 1 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 370–388 | 19 | 1 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `51` | `84` | Position_Unknown | Team_Unknown | 440–449 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 80: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [180-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-335] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-296] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-267] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-279] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-439] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-447] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-198] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-422] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-291] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-321] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-196] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-283] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-320] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-228] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-279] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-219] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-334] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-341] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-257] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-162] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-387] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-428] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-237] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-230] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-260] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-336] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-354] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-322] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-384] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-399] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-404] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-332] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-360] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-323] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-425] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-449] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-415] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-437] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-377] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-386] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-414] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-431] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-352] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-387] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-362] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-377] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-397] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-364] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-388] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>