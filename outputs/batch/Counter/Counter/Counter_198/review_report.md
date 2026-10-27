# Play-Annotation-Generator Annotation Review — Counter_198

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_198`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 168 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 127 | START | 127 | 142 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `11` | `10` | 128 | START | 172 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `2` | `1` | 128 | START | 128 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `3` | `2` | 128 | START | 128 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `5` | `4` | 128 | START | 128 | 168 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `1` | `0` | 128 | START | 128 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 143 | END | 127 | 143 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 156 | START | 156 | 172 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 173 | START | 173 | 286 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 210 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 156 | 172 | 17 | inferred_complete_timeline |
| `Action_None` | 173 | 212 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 172 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 173 | 286 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 128 | 210 | 83 | inferred_complete_timeline |
| `Action_None` | 211 | 232 | 22 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 226 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PullBlock` | 128 | 168 | 41 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 210 | 37 | inferred_complete_timeline |
| `Action_None` | 211 | 241 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 210 | 39 | inferred_complete_timeline |
| `Action_None` | 211 | 287 | 77 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 210 | 83 | inferred_complete_timeline |
| `Action_None` | 211 | 266 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 171 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 210 | 36 | inferred_complete_timeline |
| `Action_None` | 211 | 299 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 141 | 15 | inferred_complete_timeline |
| `Action_None` | 145 | 164 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 228 | 102 | inferred_complete_timeline |
| `Action_None` | 233 | 249 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 68 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 173 | 30 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 186 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 151 | 25 | inferred_complete_timeline |
| `Action_None` | 189 | 249 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 299 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 190 | 64 | inferred_complete_timeline |
| `Action_None` | 198 | 295 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 292 | 166 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 162 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `20` | Position_Unknown | Team_Unknown | 173–222 | 45 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 190–232 | 43 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 235–299 | 52 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 236–283 | 47 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 247–299 | 36 | 5 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 249–297 | 49 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 276–294 | 14 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 292–299 | 7 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `11` (C): Annotated start 128 != Inferred start 172
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [127–143], lower_priority='Action_DownBlock' annotated_start=128, effective_Action_DownBlock_start=144.
- ⚠️ Action 'Action_None' range [211-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [128-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-292] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-286] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-162] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [127-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [172-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-226] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-68] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-173] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-232] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-261] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-297] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '24' has 1 frames without a visible bounding box.
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

</details>