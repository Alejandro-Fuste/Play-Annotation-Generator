# Play-Annotation-Generator Annotation Review — BootPass_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_110`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 3
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `22` | `20` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `22` | `20` |
| ⚠️ START CHANGED | `Action_BootAway` | Position_Unknown | Team_Unknown | `22` | `20` |
| ⚠️ START CHANGED | `Action_RunFlatRoute` | LB1 | defense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `22` | `20` |
| ✅ EXACT | `Action_SecureCatch` | LB1 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `10` | `10` | 18 | START | 18 | 56 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `12` | `12` | 18 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `3` | `3` | 18 | START | 18 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `7` | `7` | 18 | START | 18 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `9` | `9` | 18 | START | 18 | 47 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `22` | `20` | 18 | END | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 29 | START | 29 | 29 |
| ❌ MISSING SEGMENT | `Action_FakeHandoff` | Position_Unknown | `22` | `20` | 39 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BootAway` | Position_Unknown | `22` | `20` | 55 | START | 64 | 76 |
| ⚠️ START CHANGED | `Action_RunFlatRoute` | LB1 | `5` | `5` | 74 | START | 77 | 94 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `22` | `20` | 77 | START | 77 | 79 |
| ✅ EXACT | `Action_SecureCatch` | LB1 | `5` | `5` | 95 | START | 95 | 107 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_None` | 65 | 95 | 31 | inferred_complete_timeline |
| `Action_None` | 98 | 146 | 49 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 55 | 27 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 150 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 18 | 47 | 30 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 59 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 18 | 56 | 39 | inferred_complete_timeline |
| `Action_RunBlock` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_RunBlock` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 28 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 29 | 1 | inferred_complete_timeline |
| `Action_None` | 30 | 38 | 9 | inferred_complete_timeline |
| `Action_None` | 40 | 53 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 18 | 45 | 28 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 68 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 18 | 57 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 149 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 49 | 21 | inferred_complete_timeline |
| `Action_None` | 69 | 172 | 104 | inferred_complete_timeline |
| `Action_None` | 177 | 269 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 174 | 146 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 269 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 77 | 94 | 18 | inferred_complete_timeline |
| `Action_SecureCatch` | 95 | 107 | 13 | inferred_complete_timeline |
| `Action_None` | 108 | 122 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 69 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 258 | 230 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 116 | 88 | inferred_complete_timeline |
| `Action_None` | 118 | 269 | 152 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 41–59 | 18 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 41–145 | 88 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 41–269 | 162 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 56–269 | 214 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 56–67 | 12 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 58–67 | 5 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 64–79 | 16 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 70–97 | 28 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 74–191 | 118 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 78–104 | 27 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 86–152 | 61 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 95–258 | 164 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 106–122 | 17 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 106–136 | 27 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 114–269 | 152 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 146–269 | 124 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 149–269 | 99 | 4 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 157–269 | 113 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 162–269 | 105 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 163–264 | 60 | 5 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 192–221 | 30 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 206–209 | 4 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 210–269 | 48 | 4 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 258–266 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (7 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_FakeHandoff` on target `20` (Position_Unknown)
- ⚠️ `Action_BootAway` for actor_track_id `22` (Position_Unknown): Annotated start 55 != Inferred start 64
- ⚠️ `Action_RunFlatRoute` for actor_track_id `5` (LB1): Annotated start 74 != Inferred start 77

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '12' has invalid range: start=29, end=18. Clamping end to start.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [29–29], lower_priority='Action_RunBlock' annotated_start=18, effective_Action_RunBlock_start=30.
- ⚠️ Segment 'Action_SnapReceive' for track '20' has invalid range: start=64, end=18. Clamping end to start.
- ⚠️ Segment 'Action_FakeHandoff' for track '20' has invalid range: start=64, end=54. Clamping end to start.
- ⚠️ Action 'Action_None' range [29-49] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-269] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [18-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-55] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [18-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [18-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [18-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [65-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [109-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [118-121] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [125-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [133-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [152-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-269] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [64-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' for track '20' starts at frame 77, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ThrowPass' range [77-79] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-258] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-114] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-136] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-207] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-221] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-238] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>