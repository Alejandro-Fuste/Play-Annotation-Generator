# Play-Annotation-Generator Annotation Review — SplitZone_317

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_317`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 8
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT | defense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ START CHANGED | `Action_PressEdge` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | DT | `11` | `11` | 25 | START | 25 | 37 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 34 | START | 34 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 34 | START | 34 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 34 | START | 34 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 37 | END | 25 | 37 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `15` | `14` | 38 | START | 38 | 57 |
| ⚠️ START CHANGED | `Action_PressEdge` | Position_Unknown | `18` | `17` | 45 | START | 60 | 67 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 52 | START | 52 | 68 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `18` | `17` | 68 | START | 68 | 78 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 38 | 51 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 52 | 68 | 17 | inferred_complete_timeline |
| `Action_None` | 69 | 126 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 84 | 51 | inferred_complete_timeline |
| `Action_None` | 85 | 239 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 84 | 51 | inferred_complete_timeline |
| `Action_None` | 85 | 110 | 26 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 84 | 51 | inferred_complete_timeline |
| `Action_None` | 85 | 185 | 101 | inferred_complete_timeline |
| `Action_None` | 192 | 208 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 87 | 63 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 88 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_None` | 38 | 239 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 75 | 51 | inferred_complete_timeline |
| `Action_None` | 77 | 171 | 95 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 139 | 115 | inferred_complete_timeline |
| `Action_None` | 144 | 239 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 117 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–172 | 114 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 36–239 | 200 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 38–57 | 20 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 38–137 | 53 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 44–52 | 9 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 60–78 | 19 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 64–148 | 81 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 65–84 | 19 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 68–239 | 172 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 72–239 | 163 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 95–160 | 59 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 95–143 | 49 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 98–239 | 142 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 99–238 | 140 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 135–239 | 105 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 142–239 | 93 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 142–145 | 4 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 186–208 | 23 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PressEdge` for actor_track_id `18` (Position_Unknown): Annotated start 45 != Inferred start 60

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 636: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [25-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-171] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-117] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-87] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '8' starts at frame 52, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [52-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-126] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-111] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [38-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-134] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-238] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-208] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>