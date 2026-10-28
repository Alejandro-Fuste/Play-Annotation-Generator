# Play-Annotation-Generator Annotation Review — Draw_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 16 | START | 16 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 16 | START | 16 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 16 | START | 16 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 16 | START | 16 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 16 | START | 16 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 38 | START | 38 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `12` | `11` | 41 | START | 41 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `13` | 41 | START | 41 | 67 |
| ✅ EXACT | `Action_PassBlock` | LT | `4` | `3` | 41 | START | 41 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `8` | `7` | 41 | START | 53 | 119 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 52 | END | 38 | 52 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 65 | START | 65 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 88 | START | 88 | 120 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 141 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 16–166
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_None` | 53 | 64 | 12 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 65 | 87 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 120 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 163 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 16–54
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 54 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 16–80
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 80 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 16–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 141 | 101 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 16–225
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 52 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 119 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 135 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 225 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 16–212
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 141 | 34 | inferred_complete_timeline |
| `Action_None` | 142 | 212 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 16–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 67 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 132 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 16–113
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 62 | 25 | inferred_complete_timeline |
| `Action_None` | 67 | 113 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 16–184
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 184 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 55 | 18 | inferred_complete_timeline |
| `Action_None` | 57 | 106 | 50 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 16–91
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 91 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 16–230
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 155 | 118 | inferred_complete_timeline |
| `Action_None` | 165 | 230 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 16–87
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 87 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 16–208
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 38 | 173 | 136 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 16–108 | 93 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 59–87 | 29 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 118–189 | 65 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 123–239 | 117 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 203–239 | 37 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [38–52], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=53.
- ⚠️ Action 'Action_None' range [38-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-230] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-91] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-119] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-141] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-225] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-163] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-212] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-54] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-87] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-189] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>