# Play-Annotation-Generator Annotation Review — CrackToss_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_21`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 298
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 50
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_CrackBlock` | WR3 | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `21` | `20` |
| ✅ EXACT | `Action_Toss` | SAF | defense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 9 | START | 9 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 9 | START | 9 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 9 | START | 9 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 9 | START | 9 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 9 | START | 9 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 9 | START | 9 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 9 | START | 9 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 9 | START | 9 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 9 | START | 9 | 130 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 129 | START | 129 | 132 |
| ✅ EXACT | `Action_CrackBlock` | WR3 | `7` | `6` | 131 | START | 131 | 228 |
| ✅ EXACT | `Action_PullBlock` | LT | `3` | `2` | 131 | START | 131 | 228 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `21` | `20` | 132 | END | 129 | 132 |
| ✅ EXACT | `Action_Toss` | SAF | `21` | `20` | 145 | START | 145 | 165 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 166 | START | 166 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 228 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 165 | 157 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 298 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–241
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 241 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 237 | 109 | inferred_complete_timeline |
| `Action_None` | 239 | 291 | 53 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 298 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 130 | 122 | inferred_complete_timeline |
| `Action_CrackBlock` | 131 | 228 | 98 | inferred_complete_timeline |
| `Action_None` | 229 | 298 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 130 | 122 | inferred_complete_timeline |
| `Action_PullBlock` | 131 | 228 | 98 | inferred_complete_timeline |
| `Action_None` | 229 | 298 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–293
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 147 | 19 | inferred_complete_timeline |
| `Action_None` | 149 | 293 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 9–173
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_BallSnap` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 173 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–293
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 25 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 128 | 101 | inferred_complete_timeline |
| `Action_None` | 129 | 155 | 27 | inferred_complete_timeline |
| `Action_None` | 157 | 184 | 28 | inferred_complete_timeline |
| `Action_None` | 187 | 293 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 230 | 102 | inferred_complete_timeline |
| `Action_None` | 233 | 298 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–274
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 244 | 116 | inferred_complete_timeline |
| `Action_None` | 251 | 266 | 16 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 298 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–289
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 289 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–248
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_None` | 129 | 248 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 9–298
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 128 | 120 | inferred_complete_timeline |
| `Action_SnapReceive` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 144 | 12 | inferred_complete_timeline |
| `Action_Toss` | 145 | 165 | 21 | inferred_complete_timeline |
| `Action_None` | 166 | 212 | 47 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |
| `Action_None` | 243 | 298 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 9–298 | 290 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 46–258 | 213 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 188–297 | 110 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 189–194 | 4 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 277–298 | 22 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 277–279 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 284–294 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 44: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (LT) duration 98 frames exceeds threshold 90 frames [start=131, end=228].
- ⚠️ Action 'Action_None' range [129-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-230] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-298] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-25] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-128] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-155] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-293] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-244] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-289] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-298] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-298] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-297] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-298] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>