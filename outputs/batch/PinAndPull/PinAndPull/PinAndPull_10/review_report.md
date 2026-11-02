# Play-Annotation-Generator Annotation Review — PinAndPull_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_10`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 20
- **Ball Tracks:** 1
- **Action Segments:** 48
- **Validation Warnings:** 38
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 30
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 162 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 128 | START | 128 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `6` | `5` | 131 | START | 131 | 197 |
| ✅ EXACT | `Action_PullBlock` | LT | `7` | `6` | 131 | START | 131 | 211 |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | C | `14` | `13` | 131 | START | 142 | 183 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 141 | END | 128 | 141 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `2` | 148 | START | 148 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 163 | START | 163 | 203 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 211 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_SnapReceive` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_None` | 142 | 147 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 148 | 162 | 15 | inferred_complete_timeline |
| `Action_None` | 163 | 196 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 203 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 216 | 217 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 197 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 211 | 10 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PullBlock` | 131 | 211 | 81 | inferred_complete_timeline |
| `Action_None` | 212 | 219 | 8 | inferred_complete_timeline |
| `Action_None` | 222 | 238 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_BallSnap` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 142 | 183 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 222 | 95 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 195 | 68 | inferred_complete_timeline |
| `Action_None` | 197 | 239 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 161 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 38–159 | 122 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 216–239 | 23 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 0 | 72 | 47 | 64.4% | 43–44, 46–60, 63–71 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ `Action_PullLeadBlock` for actor_track_id `14` (C): Annotated start 131 != Inferred start 142
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [128–141], lower_priority='Action_PullLeadBlock' annotated_start=131, effective_Action_PullLeadBlock_start=142.
- ⚠️ Action 'Action_None' range [128-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-238] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [142-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.

</details>