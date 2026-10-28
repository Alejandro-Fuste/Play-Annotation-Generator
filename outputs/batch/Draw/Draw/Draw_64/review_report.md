# Play-Annotation-Generator Annotation Review — Draw_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_64`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 65
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 9
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RG | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 3 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `5` | `4` | 12 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | `10` | `9` | 18 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `12` | `11` | 18 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | `13` | `12` | 18 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `5` | `4` | 18 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RG | `6` | `5` | 18 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `11` | `10` | 29 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 40 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `11` | `10` | 87 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 87 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 31 | 252 | 222 | inferred_complete_timeline |
| `Action_None` | 259 | 271 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 31 | 293 | 263 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 31 | 237 | 207 | inferred_complete_timeline |
| `Action_None` | 241 | 302 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 32–359 | 323 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 32–359 | 315 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 32–359 | 327 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 32–325 | 294 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 32–330 | 299 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 32–300 | 268 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 32–145 | 114 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 32–359 | 328 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 32–301 | 270 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 32–290 | 251 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 32–196 | 145 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 32–359 | 319 | 4 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 32–196 | 165 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 178–359 | 177 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 182–359 | 178 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 194–196 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 212–304 | 93 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 212–319 | 108 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 237–359 | 123 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 320–359 | 40 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 325–359 | 35 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 333–359 | 27 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 345–359 | 15 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 350–356 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `35` | `42` | 252 | 252 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `5` (C)
- ❌ Missing segment for action `Action_PassBlock` on target `10` (RT)
- ❌ Missing segment for action `Action_PassBlock` on target `12` (LT)
- ❌ Missing segment for action `Action_PassBlock` on target `13` (LG)
- ❌ Missing segment for action `Action_PassBlock` on target `5` (C)
- ❌ Missing segment for action `Action_PassBlock` on target `6` (RG)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (QB)
- ❌ Missing segment for action `Action_FakePassDroptoHandoff` on target `11` (QB)
- ❌ Missing segment for action `Action_BallCarry` on target `11` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 10 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '4' has invalid range: start=12, end=3. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '4' has invalid range: start=18, end=3. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '5' has invalid range: start=18, end=3. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '9' has invalid range: start=18, end=3. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '10' has invalid range: start=12, end=3. Clamping end to start.
- ⚠️ Segment 'Action_FakePassDroptoHandoff' for track '10' has invalid range: start=40, end=3. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '10' has invalid range: start=87, end=3. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '11' has invalid range: start=18, end=3. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '12' has invalid range: start=18, end=3. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-293] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-237] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-313] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-359] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-340] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-320] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-325] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-145] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-301] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-94] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-290] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-108] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-196] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-359] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-304] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-356] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>