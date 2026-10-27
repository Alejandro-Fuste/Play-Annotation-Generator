# Play-Annotation-Generator Annotation Review — CrackToss_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_37`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 1
- **Action Segments:** 78
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `15` |
| ✅ EXACT | `Action_CrackBlock` | TE1 | offense | `13` | `10` |
| ✅ EXACT | `Action_PullBlock` | TE2 | offense | `1` | `0` |
| ✅ EXACT | `Action_PullBlock` | CB4 | defense | `15` | `12` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `20` | `17` |
| ✅ EXACT | `Action_Toss` | DE1 | defense | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `23` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 19 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 19 | START | 20 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 19 | START | 20 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 19 | START | 20 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `23` | `Group` | 19 | START | 20 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `24` | `Group` | 19 | START | 20 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 19 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 19 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `15` | 36 | START | 36 | 45 |
| ✅ EXACT | `Action_CrackBlock` | TE1 | `13` | `10` | 39 | START | 39 | 120 |
| ✅ EXACT | `Action_PullBlock` | TE2 | `1` | `0` | 39 | START | 39 | 120 |
| ✅ EXACT | `Action_PullBlock` | CB4 | `15` | `12` | 39 | START | 39 | 120 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `20` | `17` | 45 | END | 36 | 45 |
| ✅ EXACT | `Action_Toss` | DE1 | `20` | `17` | 47 | START | 47 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `23` | `20` | 68 | START | 68 | 140 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `23`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 20–150
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 67 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 140 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 150 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 20–31
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 31 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–150
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 84 | 49 | inferred_complete_timeline |
| `Action_None` | 92 | 150 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_CrackBlock` | 39 | 120 | 82 | inferred_complete_timeline |
| `Action_None` | 121 | 150 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PullBlock` | 39 | 120 | 82 | inferred_complete_timeline |
| `Action_None` | 121 | 150 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_None` | 60 | 82 | 23 | inferred_complete_timeline |
| `Action_None` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_None` | 98 | 103 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 20–150
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 45 | 10 | inferred_complete_timeline |
| `Action_None` | 46 | 95 | 50 | inferred_complete_timeline |
| `Action_None` | 100 | 150 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 20–98
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 45 | 10 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_Toss` | 47 | 67 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 98 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 20–65
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 65 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 35 | 27 | inferred_complete_timeline |
| `Action_None` | 36 | 113 | 78 | inferred_complete_timeline |
| `Action_None` | 115 | 150 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 122 | 87 | inferred_complete_timeline |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 20–148
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 148 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 20–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 20–150
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–28
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 28 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 20–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 38 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 39 | 120 | 82 | inferred_complete_timeline |
| `Action_None` | 121 | 141 | 21 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–138 | 139 | 2 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–19 | 20 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–19 | 20 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 20–130 | 109 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 20–121 | 98 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 20–150 | 131 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 23–26 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 44–47 | 4 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 70–150 | 81 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 81–98 | 18 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 109–118 | 8 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 123–148 | 26 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 123–148 | 24 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 123–127 | 4 | 2 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 136–144 | 5 | 2 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 139–148 | 9 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `27` | 20 | 22 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 76: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ Row 76: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [121-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-58] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-82] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [39-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-84] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-65] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-98] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-148] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
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

</details>