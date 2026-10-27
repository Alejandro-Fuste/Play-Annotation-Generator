# Play-Annotation-Generator Annotation Review — CrackToss_1

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_1`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 298
- **Player Tracks:** 16
- **Ball Tracks:** 0
- **Action Segments:** 50
- **Validation Warnings:** 44
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 4
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_CrackBlock` | CB1 | defense | `3` | `0` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `7` |
| ℹ️ GLOBAL EVENT | `Action_CrackBlock` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `4` | `1` |
| ✅ EXACT | `Action_Toss` | QB1 | offense | `4` | `1` |
| ✅ EXACT | `Action_BallCarry` | CB2 | defense | `5` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 25 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `4` | `Group` | 0 | START | 25 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 25 | 35 |
| ⚠️ START CHANGED | `Action_CrackBlock` | CB1 | `3` | `0` | 9 | START | 11 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `7` | 36 | START | 36 | 48 |
| ℹ️ GLOBAL EVENT | `Action_CrackBlock` | N/A | N/A | N/A | 48 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `4` | `1` | 48 | END | 36 | 48 |
| ✅ EXACT | `Action_Toss` | QB1 | `4` | `1` | 59 | START | 59 | 77 |
| ✅ EXACT | `Action_BallCarry` | CB2 | `5` | `2` | 78 | START | 78 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 124 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `4`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 25–294
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_None` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_Toss` | 59 | 77 | 19 | inferred_complete_timeline |
| `Action_None` | 78 | 277 | 200 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |
| `Action_None` | 287 | 294 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 36 | 298 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_None` | 49 | 298 | 250 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 36 | 298 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 36 | 298 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–24
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 11 | 24 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 77 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 298 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 36 | 298 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–298
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 36 | 298 | 263 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `12` | Position_Unknown | Team_Unknown | 25–268 | 244 | 2 | Undefined position; Undefined team |
| `10` | `13` | Position_Unknown | Team_Unknown | 25–295 | 271 | 2 | Undefined position; Undefined team |
| `11` | `14` | Position_Unknown | Team_Unknown | 25–298 | 180 | 6 | Undefined position; Undefined team |
| `12` | `15` | Position_Unknown | Team_Unknown | 25–274 | 158 | 5 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 53–294 | 172 | 8 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 168–192 | 22 | 2 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 277–298 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CrackBlock` for actor_track_id `3` (CB1): Annotated start 9 != Inferred start 11

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_PullBlock' at frame 51 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 26 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '2' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '1' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [11-24] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-268] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-263] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-264] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-298] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.

</details>