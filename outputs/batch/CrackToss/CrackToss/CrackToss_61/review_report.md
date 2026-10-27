# Play-Annotation-Generator Annotation Review — CrackToss_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_61`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 1
- **Action Segments:** 80
- **Validation Warnings:** 111
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `23` | `20` |
| ✅ EXACT | `Action_CrackBlock` | WR | offense | `20` | `17` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `22` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `29` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | Position_Unknown | Team_Unknown | `29` | `24` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `16` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 16 | START | 16 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `20` | `Group` | 16 | START | 16 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 16 | START | 16 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 16 | START | 16 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 16 | START | 0 | 2 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `23` | `20` | 34 | START | 34 | 39 |
| ✅ EXACT | `Action_CrackBlock` | WR | `20` | `17` | 37 | START | 37 | 85 |
| ✅ EXACT | `Action_PullBlock` | RT | `22` | `19` | 37 | START | 37 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | `29` | `24` | 39 | END | 34 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | Position_Unknown | `29` | `24` | 47 | START | 47 | 48 |
| ✅ EXACT | `Action_BallCarry` | RB | `16` | `13` | 67 | START | 67 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 88 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 16–150
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 66 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 67 | 150 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 16–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_CrackBlock` | 37 | 85 | 49 | inferred_complete_timeline |
| `Action_None` | 105 | 150 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 67 | 34 | inferred_complete_timeline |
| `Action_None` | 75 | 103 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 16–150
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 55 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 141 | 73 | inferred_complete_timeline |
| `Action_None` | 143 | 150 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 16–150
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 37 | 88 | 52 | inferred_complete_timeline |
| `Action_None` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 16–150
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_None` | 34 | 150 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 33 | 21 | inferred_complete_timeline |
| `Action_None` | 34 | 83 | 50 | inferred_complete_timeline |
| `Action_None` | 90 | 109 | 20 | inferred_complete_timeline |
| `Action_None` | 116 | 132 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 16–68
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 68 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 16–150
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 150 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 16–150
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 150 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 16–150
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 113 | 80 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–15 | 16 | 1 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–15 | 16 | 1 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–128 | 103 | 6 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–5 | 6 | 1 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–150 | 143 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–97 | 21 | 3 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–83 | 30 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–15 | 7 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 16–85 | 70 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 21–150 | 130 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 23–51 | 19 | 7 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 45–150 | 106 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 56–78 | 23 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 76–150 | 75 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 81–93 | 13 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 82–95 | 14 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 86–150 | 63 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 97–107 | 11 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 112–150 | 38 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 116–145 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | 16 | 33 | 10 | 55.6% | 21–24, 27–29, 31 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `29` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `29` (2 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 124: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-27] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-66] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-150] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-8] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-83] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [37-85] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-85] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-33] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' for track '24' starts at frame 34, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SnapReceive' range [34-34] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [36-38] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-46] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [47-48] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [50-51] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-78] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-95] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-95] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-150] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-107] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-141] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-150] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>