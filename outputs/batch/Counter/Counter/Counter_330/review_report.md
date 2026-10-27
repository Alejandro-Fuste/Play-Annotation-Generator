# Play-Annotation-Generator Annotation Review — Counter_330

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_330`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | defense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 56 | START | 56 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT2 | `13` | `12` | 59 | START | 59 | 115 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `5` | `4` | 59 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 59 | START | 59 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `12` | `11` | 59 | START | 59 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | WR | `14` | `13` | 59 | START | 59 | 95 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `5` | `4` | 67 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | `5` | `4` | 86 | START | 86 | 93 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `10` | `9` | 105 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 102 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 94 | 39 | inferred_complete_timeline |
| `Action_None` | 96 | 103 | 8 | inferred_complete_timeline |
| `Action_None` | 108 | 299 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 59 | 95 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 121 | 63 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 153 | 28 | inferred_complete_timeline |
| `Action_None` | 154 | 173 | 20 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 197 | 279 | 83 | inferred_complete_timeline |
| `Action_None` | 281 | 291 | 11 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PullBlock` | 59 | 81 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BallSnap` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_None` | 68 | 85 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 252 | 118 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 125 | 49 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 299 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 198 | 143 | inferred_complete_timeline |
| `Action_None` | 200 | 246 | 47 | inferred_complete_timeline |
| `Action_None` | 249 | 295 | 47 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 139 | 84 | inferred_complete_timeline |
| `Action_None` | 150 | 178 | 29 | inferred_complete_timeline |
| `Action_None` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 123 | 68 | inferred_complete_timeline |
| `Action_None` | 151 | 172 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 115 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 143 | 88 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 299 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 299 | 244 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–136 | 137 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 73–197 | 116 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 77–124 | 48 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 90–151 | 57 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 110–125 | 16 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 114–183 | 70 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 116–151 | 21 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 122–299 | 177 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 130–178 | 29 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 132–299 | 155 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 140–298 | 157 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 171–299 | 117 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 177–299 | 122 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 177–299 | 123 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 191–299 | 109 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 194–299 | 85 | 9 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 201–206 | 5 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 210–299 | 89 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 210–299 | 89 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 213–299 | 87 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 222–299 | 78 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 228–299 | 15 | 5 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `5` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `5` (C)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 662: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '4' has invalid range: start=59, end=55. Clamping end to start.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [56–67], lower_priority='Action_DownBlock' annotated_start=59, effective_Action_DownBlock_start=68.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [56–67], lower_priority='Action_SnapReceive' annotated_start=56, effective_Action_SnapReceive_start=68.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 95 frames exceeds threshold 90 frames [start=59, end=153].
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=105, end=102. Clamping end to start.
- ⚠️ Action 'Action_None' range [56-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-178] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-172] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [86-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [95-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-279] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-291] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-295] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [59-81] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [83-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [59-95] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [99-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-125] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-184] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-151] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-183] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-264] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-284] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-282] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-298] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-194] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-218] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-219] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-275] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-287] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-251] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>