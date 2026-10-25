# Play-Annotation-Generator Annotation Review — BootPass_124

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_124`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `23` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | Team_Unknown | `23` | `20` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | DT1 | defense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | CB | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `10` | `10` | 30 | START | 30 | 50 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `10` | `10` | 79 | START | 80 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `3` | `3` | 79 | START | 79 | 346 |
| ✅ EXACT | `Action_RunBlock` | LG | `4` | `4` | 79 | START | 79 | 359 |
| ✅ EXACT | `Action_RunBlock` | RT | `5` | `5` | 79 | START | 79 | 359 |
| ✅ EXACT | `Action_RunBlock` | RG | `9` | `9` | 79 | START | 79 | 359 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `23` | `20` | 79 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | `23` | `20` | 114 | START | 118 | 151 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `22` | `19` | 120 | START | 120 | 171 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | DT1 | `16` | `16` | 174 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | CB | `8` | `8` | 197 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 160 | 131 | inferred_complete_timeline |
| `Action_None` | 166 | 359 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 116 | 87 | inferred_complete_timeline |
| `Action_None` | 124 | 359 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 359 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 359 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 346 | 268 | inferred_complete_timeline |
| `Action_RunBlock` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 359 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_BallSnap` | 30 | 50 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 79 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 359 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 359 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 359 | 281 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 154 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 139 | 110 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_None` | 157 | 161 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 287 | 98 | inferred_complete_timeline |
| `Action_None` | 289 | 359 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 118 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 46 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 245 | 216 | inferred_complete_timeline |
| `Action_None` | 248 | 281 | 34 | inferred_complete_timeline |
| `Action_None` | 296 | 301 | 6 | inferred_complete_timeline |
| `Action_None` | 306 | 310 | 5 | inferred_complete_timeline |
| `Action_None` | 314 | 320 | 7 | inferred_complete_timeline |
| `Action_None` | 326 | 359 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 67 | 38 | inferred_complete_timeline |
| `Action_None` | 69 | 112 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 267 | 238 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 359 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 49 | 20 | inferred_complete_timeline |
| `Action_None` | 51 | 199 | 149 | inferred_complete_timeline |
| `Action_None` | 204 | 227 | 24 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `21` | Position_Unknown | Team_Unknown | 108–118 | 11 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 111–358 | 242 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 118–359 | 214 | 6 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–358 | 232 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 131–146 | 16 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 135–359 | 225 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 144–359 | 201 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 160–359 | 169 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 199–359 | 157 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 245–328 | 74 | 6 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 246–250 | 5 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 248–265 | 15 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 280–295 | 6 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 312–359 | 48 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 315–359 | 42 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 318–359 | 31 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 335–355 | 21 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 347–355 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `10` (2 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `10` (C): Annotated start 79 != Inferred start 80
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `20` (4 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `16` (DT1)
- ❌ Missing segment for action `Action_SecureCatch` on target `8` (CB)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_SecureCatch' for track '8' has invalid range: start=197, end=126. Clamping end to start.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [30–79], lower_priority='Action_RunBlock' annotated_start=79, effective_Action_RunBlock_start=80.
- ⚠️ Segment 'Action_ThrowPass' for track '16' has invalid range: start=174, end=118. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '20' has invalid range: start=118, end=79. Clamping end to start.
- ⚠️ Action 'Action_None' range [30-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-281] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [79-346] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [351-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-116] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [79-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [30-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-49] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-343] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-358] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [118-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [154-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [166-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-358] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-319] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-325] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-355] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-355] for track '36' has 2 frames without a visible bounding box.
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