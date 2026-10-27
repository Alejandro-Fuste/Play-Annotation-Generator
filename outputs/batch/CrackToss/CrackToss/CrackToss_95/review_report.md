# Play-Annotation-Generator Annotation Review — CrackToss_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_95`
- **Frame Range:** 0 to 249 (250 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 249
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 125
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RB2 | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `4` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `6` | `Group` | 0 | START | 0 | 149 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 120 | START | 120 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `19` | `18` | 123 | START | 123 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `3` | `2` | 123 | START | 123 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RB2 | `4` | `3` | 123 | START | 123 | 172 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 123 | END | 120 | 123 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 126 | START | 126 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `6` | `5` | 150 | START | 150 | 175 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 217 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 119 | 108 | inferred_complete_timeline |
| `Action_SnapReceive` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_Toss` | 126 | 149 | 24 | inferred_complete_timeline |
| `Action_None` | 150 | 249 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 175 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 212 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 238 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PullBlock` | 123 | 172 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 177 | 197 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_None` | 218 | 241 | 24 | inferred_complete_timeline |
| `Action_None` | 243 | 249 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_CrackBlock` | 123 | 170 | 48 | inferred_complete_timeline |
| `Action_CrackBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_CrackBlock` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_CrackBlock` | 182 | 197 | 16 | inferred_complete_timeline |
| `Action_CrackBlock` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 249 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 170 | 51 | inferred_complete_timeline |
| `Action_None` | 177 | 197 | 21 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 230 | 9 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 246 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 119 | 68 | inferred_complete_timeline |
| `Action_None` | 120 | 249 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 173 | 54 | inferred_complete_timeline |
| `Action_None` | 175 | 208 | 34 | inferred_complete_timeline |
| `Action_None` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 249 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 25 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 119 | 93 | inferred_complete_timeline |
| `Action_None` | 120 | 194 | 75 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 249 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 217 | 98 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 249 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 249 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–242 | 215 | 6 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–246 | 196 | 14 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–245 | 240 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–149 | 142 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–147 | 138 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–197 | 173 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–238 | 166 | 10 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–133 | 105 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 13–249 | 225 | 7 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 39–194 | 139 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 132–167 | 32 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 183–197 | 15 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 183–188 | 6 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 213–249 | 37 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 216–244 | 22 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 216–249 | 34 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 220–249 | 30 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 228–249 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (6 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (5 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 114 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 192: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 192: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '3' (RB2) duration 95 frames exceeds threshold 90 frames [start=123, end=217].
- ⚠️ Action 'Action_None' range [120-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-242] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-217] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [123-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [172-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [177-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [182-197] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [211-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [123-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [177-197] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [202-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [211-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-241] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-175] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [177-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-238] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-25] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-194] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-249] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-170] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-197] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-41] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-197] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-230] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-237] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-119] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-144] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-119] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-45] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [123-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [172-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [175-194] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [196-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-49] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-45] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-173] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-194] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-197] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-249] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>