# Play-Annotation-Generator Annotation Review — CrackToss_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_16`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 42 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `15` | 43 | START | 52 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `4` | `3` | 47 | START | 47 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `2` | `1` | 47 | START | 47 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 47 | END | 43 | 47 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 59 | START | 59 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `1` | `0` | 77 | START | 77 | 149 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 47 | 5 | inferred_complete_timeline |
| `Action_None` | 48 | 58 | 11 | inferred_complete_timeline |
| `Action_Toss` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_None` | 77 | 96 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 72 | 30 | inferred_complete_timeline |
| `Action_None` | 76 | 91 | 16 | inferred_complete_timeline |
| `Action_None` | 93 | 150 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 47 | 73 | 27 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 85 | 150 | 66 | inferred_complete_timeline |
| `Action_None` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 180 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 149 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 173 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 180 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_None` | 43 | 51 | 9 | inferred_complete_timeline |
| `Action_None` | 53 | 95 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 53 | 11 | inferred_complete_timeline |
| `Action_None` | 56 | 63 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 55 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 78 | 36 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 106 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 83 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–80 | 78 | 3 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–180 | 179 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 27–180 | 135 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 52–180 | 129 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 56–58 | 3 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 74–160 | 67 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 79–180 | 97 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 86–180 | 80 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 89–90 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 97–125 | 27 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 107–180 | 72 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 119–150 | 19 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 126–168 | 43 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 128–172 | 7 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 129–180 | 49 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 142–161 | 13 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 151–180 | 27 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 152–180 | 29 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 154–180 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 43 != Inferred start 52
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (LT) duration 104 frames exceeds threshold 90 frames [start=47, end=150].
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=52, end=47. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [47-73] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [85-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [47-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [78-80] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-159] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-51] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-95] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-96] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-63] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-106] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-140] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-180] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-130] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-145] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-168] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>