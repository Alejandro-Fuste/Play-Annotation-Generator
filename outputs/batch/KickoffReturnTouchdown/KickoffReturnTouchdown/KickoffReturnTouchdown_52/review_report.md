# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_52

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_52`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 419
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 45
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
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchKick` | Front_Blocker5 | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Front_Blocker5 | defense | `10` | `10` |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker5 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `13` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `18` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `2` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `20` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `21` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `5` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `6` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 117 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `16` | `16` | 118 | START | 118 | 166 |
| ✅ EXACT | `Action_KickBall` | Kicker | `16` | `16` | 167 | START | 167 | 172 |
| ✅ EXACT | `Action_CatchKick` | Front_Blocker5 | `10` | `10` | 217 | START | 217 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Front_Blocker5 | `10` | `10` | 242 | START | 242 | 399 |
| ✅ EXACT | `Action_CrossGoalLine` | Front_Blocker5 | `10` | `10` | 400 | START | 400 | 411 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_KickApproach` | 118 | 166 | 49 | inferred_complete_timeline |
| `Action_KickBall` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 173 | 214 | 42 | inferred_complete_timeline |
| `Action_None` | 222 | 419 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 195 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 213 | 96 | inferred_complete_timeline |
| `Action_None` | 221 | 360 | 140 | inferred_complete_timeline |
| `Action_None` | 364 | 419 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 133 | 16 | inferred_complete_timeline |
| `Action_None` | 137 | 419 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 271 | 154 | inferred_complete_timeline |
| `Action_None` | 278 | 366 | 89 | inferred_complete_timeline |
| `Action_None` | 368 | 419 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 419 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 263 | 146 | inferred_complete_timeline |
| `Action_None` | 278 | 419 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 226 | 109 | inferred_complete_timeline |
| `Action_None` | 231 | 242 | 12 | inferred_complete_timeline |
| `Action_None` | 247 | 352 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 416 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 235 | 118 | inferred_complete_timeline |
| `Action_None` | 237 | 367 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 419 | 302 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 293 | 176 | inferred_complete_timeline |
| `Action_None` | 298 | 419 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 419 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–390
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 390 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 380 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_CatchKick` | 217 | 228 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 241 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 242 | 399 | 158 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 400 | 411 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 412 | 419 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 238 | 121 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_None` | 253 | 419 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 279 | 162 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 294 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 246 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 419 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 383 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_None` | 118 | 419 | 302 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 96–97 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 203–211 | 9 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 206–419 | 214 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 333–335 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 382–419 | 38 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 32 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [118-383] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-367] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-416] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-352] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-390] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-360] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-271] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-366] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-279] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-419] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-380] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-419] for track '27' has 2 frames without a visible bounding box.
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

</details>