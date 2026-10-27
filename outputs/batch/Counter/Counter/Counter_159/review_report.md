# Play-Annotation-Generator Annotation Review — Counter_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_159`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `18` | 123 | START | 123 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 133 | START | 133 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 133 | START | 133 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 133 | START | 133 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 133 | START | 133 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | QB | `8` | `7` | 133 | START | 133 | 194 |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | `17` | `16` | 136 | START | 136 | 176 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `15` | `14` | 139 | END | 123 | 139 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `15` | `14` | 154 | START | 154 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 177 | START | 177 | 208 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 221 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 133 | 194 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 215 | 221 | 7 | inferred_complete_timeline |
| `Action_None` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 189 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 270 | 148 | inferred_complete_timeline |
| `Action_None` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_None` | 276 | 293 | 18 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 197 | 75 | inferred_complete_timeline |
| `Action_None` | 200 | 296 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 299 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 181 | 59 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–299 | 293 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–299 | 300 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–299 | 290 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–299 | 299 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–132 | 133 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–299 | 240 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–299 | 297 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–197 | 187 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 173–177 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 195–299 | 105 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 206–258 | 47 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 225–299 | 74 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 268–299 | 18 | 6 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '18' has invalid range: start=133, end=132. Clamping end to start.
- ⚠️ Action 'Action_None' range [123-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-296] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [133-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 123, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [123-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-209] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [154-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-276] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [123-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-202] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [133-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [189-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [194-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-291] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>