# Play-Annotation-Generator Annotation Review — InsideZoneRead_183

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_183`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 49
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 9
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 35
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | LB2 | defense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | LB2 | defense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_Handoff` | LB2 | defense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 218 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `20` | `18` | 371 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `11` | `10` | 374 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `12` | `11` | 374 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `3` | `2` | 374 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `4` | `3` | 374 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | LB2 | `14` | `13` | 387 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | LB2 | `14` | `13` | 391 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Handoff` | LB2 | `14` | `13` | 416 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `16` | `15` | 423 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 460 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 164 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 186 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 204 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 126 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 171 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 269 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 66–183 | 46 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 87–189 | 103 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 118–180 | 43 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 132–147 | 16 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 143–269 | 122 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 153–269 | 114 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 155–201 | 46 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 160–172 | 13 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 175–178 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 176–269 | 88 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 202–217 | 16 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `3` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `4` (RT)
- ❌ Missing segment for action `Action_SnapReceive` on target `14` (LB2)
- ❌ Missing segment for action `Action_ReadDefender` on target `14` (LB2)
- ❌ Missing segment for action `Action_Handoff` on target `14` (LB2)
- ❌ Missing segment for action `Action_BallCarry` on target `16` (Position_Unknown)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 10 |
| Other | 12 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 366: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '2' has invalid range: start=374, end=168. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '3' has invalid range: start=374, end=204. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=374, end=178. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=374, end=140. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '13' has invalid range: start=371, end=91. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '13' has invalid range: start=391, end=91. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '13' has invalid range: start=416, end=91. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '15' has invalid range: start=423, end=189. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=371, end=147. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-189] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-189] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-172] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-189] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-217] for track '25' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_BallSnap' has invalid start frame 371. Video range is [0, 269].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 374. Video range is [0, 269].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 374. Video range is [0, 269].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 374. Video range is [0, 269].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 374. Video range is [0, 269].
- ⚠️ Action event 'Action_SnapReceive' has invalid start frame 387. Video range is [0, 269].
- ⚠️ Action event 'Action_ReadDefender' has invalid start frame 391. Video range is [0, 269].
- ⚠️ Action event 'Action_Handoff' has invalid start frame 416. Video range is [0, 269].
- ⚠️ Action event 'Action_BallCarry' has invalid start frame 423. Video range is [0, 269].
- ⚠️ Action event 'Action_None' has invalid start frame 460. Video range is [0, 269].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_183'; source metadata written as null.

</details>