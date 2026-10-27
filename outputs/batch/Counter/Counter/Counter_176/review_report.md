# Play-Annotation-Generator Annotation Review — Counter_176

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_176`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR3 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 55 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `13` | `12` | 10 | START | 10 | 27 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LG | `11` | `10` | 12 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR3 | `3` | `2` | 12 | START | 12 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 12 | START | 12 | 43 |
| ✅ EXACT | `Action_SnapReceive` | LG | `11` | `10` | 27 | END | 10 | 27 |
| ✅ EXACT | `Action_Handoff` | LG | `11` | `10` | 37 | START | 37 | 55 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `9` | `8` | 56 | START | 56 | 68 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 107 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 68 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 94 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 12 | 30 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 34 | 49 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 12 | 43 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 46 | 60 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 101 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 36 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 37 | 55 | 19 | inferred_complete_timeline |
| `Action_None` | 56 | 116 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 59–143
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 59 | 143 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 59 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 160 | 151 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 39 | 12 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 52–113
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 113 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 96 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 97 | 88 | inferred_complete_timeline |
| `Action_None` | 99 | 153 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 140 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 73 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `22`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 72–239
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 72 | 84 | 13 | inferred_complete_timeline |
| `Action_None` | 86 | 145 | 60 | inferred_complete_timeline |
| `Action_None` | 147 | 237 | 91 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–98 | 99 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 89–119 | 30 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 102–200 | 99 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 120–149 | 26 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 122–166 | 40 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 151–239 | 83 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 152–166 | 15 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 216–224 | 5 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `11` (LG)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `22`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 353: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [10-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [12-30] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [34-49] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [12-43] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [46-60] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-160] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-96] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-237] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-166] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>