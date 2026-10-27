# Play-Annotation-Generator Annotation Review — Counter_262

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_262`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 81
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | DE2 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 31 | START | 31 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 34 | START | 47 | 56 |
| ✅ EXACT | `Action_DownBlock` | DE2 | `5` | `4` | 34 | START | 34 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `12` | `11` | 34 | START | 34 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `6` | `5` | 34 | START | 34 | 54 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 46 | END | 31 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `2` | `1` | 77 | START | 77 | 145 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 125 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_None` | 47 | 76 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 145 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 181 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 262 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 70 | 40 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 34 | 54 | 21 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 56 | 125 | 70 | inferred_complete_timeline |
| `Action_None` | 126 | 141 | 16 | inferred_complete_timeline |
| `Action_None` | 143 | 194 | 52 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 208 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 34 | 49 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 125 | 57 | inferred_complete_timeline |
| `Action_None` | 126 | 158 | 33 | inferred_complete_timeline |
| `Action_None` | 166 | 299 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 105 | 40 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 66 | 36 | inferred_complete_timeline |
| `Action_None` | 107 | 169 | 63 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 70 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 105 | 75 | inferred_complete_timeline |
| `Action_None` | 112 | 141 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 34 | 125 | 92 | inferred_complete_timeline |
| `Action_None` | 126 | 138 | 13 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 157 | 12 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 40 | 10 | inferred_complete_timeline |
| `Action_None` | 56 | 133 | 78 | inferred_complete_timeline |
| `Action_None` | 136 | 155 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 93 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 53 | 23 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 299 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 31 | 101 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–87 | 70 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 35–120 | 82 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 50–149 | 94 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 77–299 | 218 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 114–144 | 8 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 133–299 | 167 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 134–141 | 8 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 179–299 | 118 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 277–299 | 23 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 16 | 33 | 9 | 50.0% | 20–21, 24–30 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 526: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (DE2) duration 92 frames exceeds threshold 90 frames [start=34, end=125].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (LG) duration 92 frames exceeds threshold 90 frames [start=34, end=125].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 92 frames exceeds threshold 90 frames [start=34, end=125].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_DownBlock' annotated_start=34, effective_Action_DownBlock_start=47.
- ⚠️ Action 'Action_None' range [31-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [34-54] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [56-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-56] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [34-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [53-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-141] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>