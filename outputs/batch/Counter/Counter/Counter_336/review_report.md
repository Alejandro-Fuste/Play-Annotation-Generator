# Play-Annotation-Generator Annotation Review — Counter_336

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_336`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 48 | START | 48 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `3` | `2` | 51 | START | 51 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `4` | `3` | 51 | START | 51 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 51 | START | 51 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `14` | `13` | 51 | START | 66 | 67 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `9` | `8` | 51 | START | 51 | 141 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 65 | END | 48 | 65 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 77 | START | 77 | 100 |
| ✅ EXACT | `Action_BallCarry` | RB | `1` | `0` | 101 | START | 101 | 147 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 141 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 65 | 18 | inferred_complete_timeline |
| `Action_None` | 66 | 76 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 100 | 24 | inferred_complete_timeline |
| `Action_None` | 101 | 146 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 147 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 119 | 72 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 141 | 91 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 71 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_None` | 142 | 160 | 19 | inferred_complete_timeline |
| `Action_None` | 164 | 209 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 77 | 141 | 65 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 74 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_None` | 142 | 204 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 51 | 141 | 91 | inferred_complete_timeline |
| `Action_None` | 142 | 210 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 197 | 150 | inferred_complete_timeline |
| `Action_None` | 200 | 208 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_None` | 70 | 97 | 28 | inferred_complete_timeline |
| `Action_None` | 100 | 170 | 71 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 54 | 7 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 55 | 8 | inferred_complete_timeline |
| `Action_None` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_None` | 86 | 210 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 47 | 21 | inferred_complete_timeline |
| `Action_None` | 48 | 110 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `17` | Position_Unknown | Team_Unknown | 22–210 | 122 | 4 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 25–141 | 94 | 4 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 79–88 | 10 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 79–83 | 4 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 92–115 | 24 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 133–210 | 78 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 148–209 | 57 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 154–208 | 55 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 158–210 | 38 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 176–210 | 35 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (LT) duration 91 frames exceeds threshold 90 frames [start=51, end=141].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LG) duration 91 frames exceeds threshold 90 frames [start=51, end=141].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (RG) duration 91 frames exceeds threshold 90 frames [start=51, end=141].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '13' (C) duration 91 frames exceeds threshold 90 frames [start=51, end=141].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [48–65], lower_priority='Action_PullBlock' annotated_start=51, effective_Action_PullBlock_start=66.
- ⚠️ Action 'Action_BallCarry' range [101-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [51-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [51-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-141] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [51-74] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-170] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [51-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-146] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [48-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [66-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-115] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '24' has 1 frames without a visible bounding box.
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

</details>