# Play-Annotation-Generator Annotation Review — BootPass_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_131`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_FakeHandoff` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_RunFlatRoute` | LB3 | defense | `13` | `13` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `25` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `9` | `9` | 23 | START | 23 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `15` | `15` | 48 | START | 48 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `18` | `18` | 48 | START | 48 | 80 |
| ✅ EXACT | `Action_RunBlock` | LT | `20` | `20` | 48 | START | 48 | 329 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RT | `8` | `8` | 48 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `9` | `9` | 48 | START | 59 | 60 |
| ✅ EXACT | `Action_SnapReceive` | RT | `8` | `8` | 58 | END | 23 | 58 |
| ✅ EXACT | `Action_FakeHandoff` | RT | `8` | `8` | 66 | START | 66 | 69 |
| ✅ EXACT | `Action_ThrowPass` | RT | `8` | `8` | 70 | START | 70 | 79 |
| ✅ EXACT | `Action_BootAway` | QB | `10` | `10` | 80 | START | 80 | 140 |
| ✅ EXACT | `Action_RunFlatRoute` | LB3 | `13` | `13` | 86 | START | 86 | 153 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `25` | `24` | 89 | START | 125 | 125 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_BootAway` | 80 | 140 | 61 | inferred_complete_timeline |
| `Action_None` | 141 | 244 | 104 | inferred_complete_timeline |
| `Action_None` | 248 | 329 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 316 | 294 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 223 | 201 | inferred_complete_timeline |
| `Action_None` | 225 | 228 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 235 | 213 | inferred_complete_timeline |
| `Action_None` | 237 | 272 | 36 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 302 | 306 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 329 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 329 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 80 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 94 | 201 | 108 | inferred_complete_timeline |
| `Action_RunBlock` | 205 | 212 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 226 | 329 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 46 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 180 | 113 | inferred_complete_timeline |
| `Action_RunBlock` | 183 | 189 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 196 | 149 | inferred_complete_timeline |
| `Action_RunBlock` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 209 | 329 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 58 | 36 | inferred_complete_timeline |
| `Action_None` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_FakeHandoff` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_None` | 80 | 329 | 250 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 176 | 154 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 260 | 52 | inferred_complete_timeline |
| `Action_None` | 262 | 329 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 242 | 220 | inferred_complete_timeline |
| `Action_None` | 244 | 257 | 14 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 79 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 123 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 329 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 329 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 86 | 153 | 68 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 258 | 236 | inferred_complete_timeline |
| `Action_None` | 266 | 270 | 5 | inferred_complete_timeline |
| `Action_None` | 273 | 286 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 329 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 73 | 51 | inferred_complete_timeline |
| `Action_None` | 76 | 329 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 290 | 268 | inferred_complete_timeline |
| `Action_None` | 295 | 329 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–188 | 188 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–329 | 235 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 89–90 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 125–329 | 202 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 209–329 | 121 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 239–329 | 91 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 310–329 | 19 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 318–329 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (6 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `8` (RT)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (4 segments found)
- ⚠️ `Action_SecureCatch` for actor_track_id `25` (Position_Unknown): Annotated start 89 != Inferred start 125

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 242: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_RunBlock' for track '8' has invalid range: start=48, end=22. Clamping end to start.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [23–58], lower_priority='Action_RunBlock' annotated_start=48, effective_Action_RunBlock_start=59.
- ⚠️ Segment 'Action_SecureCatch' for track '24' has invalid range: start=125, end=107. Clamping end to start.
- ⚠️ Action 'Action_None' range [23-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-306] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-316] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-290] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-79] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [23-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [64-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [183-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-176] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-329] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' for track '15' starts at frame 48, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunBlock' range [48-196] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [201-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [209-329] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' for track '18' starts at frame 48, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_RunBlock' range [48-80] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [89-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [94-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [205-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [215-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-294] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>