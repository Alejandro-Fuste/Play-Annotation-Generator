# Play-Annotation-Generator Annotation Review — Counter_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_10`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 61 | START | 61 | 78 |
| ✅ EXACT | `Action_DownBlock` | LT | `6` | `5` | 66 | START | 66 | 158 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | TE | `4` | `3` | 66 | START | N/A | N/A |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `4` | `3` | 66 | START | 66 | 158 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `7` | `6` | 78 | END | 61 | 78 |
| ✅ EXACT | `Action_Handoff` | DE2 | `7` | `6` | 87 | START | 87 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 116 | START | 116 | 291 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 291 | 176 | inferred_complete_timeline |
| `Action_BallCarry` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 66 | 158 | 93 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 158 | 93 | inferred_complete_timeline |
| `Action_None` | 159 | 184 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 105 | 45 | inferred_complete_timeline |
| `Action_None` | 108 | 329 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 78 | 18 | inferred_complete_timeline |
| `Action_None` | 79 | 108 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 187 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 189 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 91 | 31 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 78 | 18 | inferred_complete_timeline |
| `Action_None` | 79 | 86 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 87 | 115 | 29 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 107 | 47 | inferred_complete_timeline |
| `Action_None` | 109 | 123 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 172 | 112 | inferred_complete_timeline |
| `Action_None` | 176 | 247 | 72 | inferred_complete_timeline |
| `Action_None` | 249 | 293 | 45 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 119 | 59 | inferred_complete_timeline |
| `Action_None` | 122 | 166 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 3–94 | 87 | 3 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 98–109 | 6 | 2 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 125–159 | 35 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 135–148 | 11 | 3 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 137–183 | 43 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 143–329 | 181 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 152–181 | 30 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 155–329 | 175 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 155–169 | 8 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 164–196 | 33 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 202–329 | 128 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 212–329 | 114 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 220–329 | 110 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 221–244 | 24 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 223–242 | 20 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 230–314 | 84 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 250–329 | 80 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 274–317 | 44 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 278–318 | 41 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 280–329 | 50 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 294–310 | 17 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 314–320 | 6 | 2 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PullBlock` on target `4` (TE)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 22: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Overlapping action conflict at frame 66 for track '3': 'Action_PullBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (LT) duration 93 frames exceeds threshold 90 frames [start=66, end=158].
- ⚠️ Action 'Action_None' range [61-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-291] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [294-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-189] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-247] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-293] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-91] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [61-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-108] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-86] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-159] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-183] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-203] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-310] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-196] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-242] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-317] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-318] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-310] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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