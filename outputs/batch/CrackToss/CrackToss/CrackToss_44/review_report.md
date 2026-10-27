# Play-Annotation-Generator Annotation Review — CrackToss_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | SAF | defense | `3` | `2` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 112 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 81 | START | 81 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | SAF | `3` | `2` | 84 | START | 84 | 93 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `14` | `13` | 84 | START | 92 | 122 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 95 | END | 81 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 99 | START | 99 | 112 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 113 | START | 113 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 140 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_Toss` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 113 | 175 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 148 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 120 | 40 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 175 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 97 | 112 | 16 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 121 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 166 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 115 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 175 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_CrackBlock` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_CrackBlock` | 95 | 112 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–175 | 176 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–171 | 172 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–120 | 117 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 3–169 | 47 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 35–110 | 19 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 36–40 | 4 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 94–111 | 18 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 96–136 | 14 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 97–175 | 64 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 97–107 | 11 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 97–110 | 14 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 97–110 | 14 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 99–111 | 13 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 127–144 | 8 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 144–159 | 10 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 147–175 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `14` (Position_Unknown): Annotated start 84 != Inferred start 92

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 90: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [81-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [84-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [95-112] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [81-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-112] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-121] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [92-122] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-112] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-175] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-175] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>