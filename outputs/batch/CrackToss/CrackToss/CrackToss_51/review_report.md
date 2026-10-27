# Play-Annotation-Generator Annotation Review — CrackToss_51

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_51`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 121
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_CrackBlock` | TE | offense | `23` | `22` |
| ✅ EXACT | `Action_PullBlock` | RB | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `21` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 2 | START | 3 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 2 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 2 | START | 3 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `23` | `Group` | 2 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `24` | `Group` | 2 | START | 3 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `25` | `Group` | 2 | START | 3 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `26` | `Group` | 2 | START | 3 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 2 | START | 0 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 9 | START | 9 | 22 |
| ✅ EXACT | `Action_CrackBlock` | TE | `23` | `22` | 12 | START | 12 | 79 |
| ✅ EXACT | `Action_PullBlock` | RB | `21` | `20` | 12 | START | 12 | 19 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 22 | END | 9 | 22 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 23 | START | 23 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `21` | `20` | 44 | START | 44 | 91 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 22 | 14 | inferred_complete_timeline |
| `Action_Toss` | 23 | 43 | 21 | inferred_complete_timeline |
| `Action_None` | 44 | 68 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–97
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 12 | 19 | 8 | inferred_complete_timeline |
| `Action_None` | 20 | 43 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 91 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 3–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_CrackBlock` | 12 | 79 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 3–96
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_None` | 9 | 96 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 3–125
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_None` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 86 | 59 | inferred_complete_timeline |
| `Action_None` | 98 | 125 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–61
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 22 | 14 | inferred_complete_timeline |
| `Action_None` | 23 | 61 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `26`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 3–124
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_None` | 9 | 28 | 20 | inferred_complete_timeline |
| `Action_None` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_None` | 33 | 37 | 5 | inferred_complete_timeline |
| `Action_None` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 108 | 56 | inferred_complete_timeline |
| `Action_None` | 115 | 124 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_None` | 9 | 125 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_None` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 125 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 81 | 73 | inferred_complete_timeline |
| `Action_None` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 117 | 109 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 58 | 50 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 68 | 125 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 8 | 6 | inferred_complete_timeline |
| `Action_None` | 9 | 125 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–124 | 122 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 20–30 | 11 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 39–125 | 85 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 49–125 | 76 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 55–125 | 71 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 56–73 | 18 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 59–125 | 62 | 2 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 69–80 | 12 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 76–125 | 50 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 85–104 | 20 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 91–125 | 35 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 93–118 | 26 | 1 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 100–104 | 5 | 1 | Undefined position; Undefined team |
| `39` | `42` | Position_Unknown | Team_Unknown | 105–125 | 17 | 2 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 68 targets track ID '88', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 104: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [9-58] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-125] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-81] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-124] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-94] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-125] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [12-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-26] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-28] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-37] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-30] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-63] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-89] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-73] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-96] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-80] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-125] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-104] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-125] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-118] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-114] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>