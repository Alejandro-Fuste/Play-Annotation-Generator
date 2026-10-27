# Play-Annotation-Generator Annotation Review — CrackToss_70

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_70`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 86
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE2 | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `11` | `10` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 16 | START | 16 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE2 | `14` | `13` | 19 | START | 19 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `11` | `10` | 19 | START | 19 | 150 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `12` | `11` | 19 | START | 19 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 23 | END | 16 | 23 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 27 | START | 27 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 41 | START | 41 | 99 |

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
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 23 | 8 | inferred_complete_timeline |
| `Action_None` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_Toss` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_None` | 41 | 82 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 41 | 99 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 134 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 19 | 150 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_CrackBlock` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_CrackBlock` | 44 | 45 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 23 | 8 | inferred_complete_timeline |
| `Action_None` | 24 | 67 | 44 | inferred_complete_timeline |
| `Action_None` | 69 | 150 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 80 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_None` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 38 | 109 | 72 | inferred_complete_timeline |
| `Action_None` | 111 | 138 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 89 | 74 | inferred_complete_timeline |
| `Action_None` | 93 | 104 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 59 | 44 | inferred_complete_timeline |
| `Action_None` | 62 | 150 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 150 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 63 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 103 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 109 | 94 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–150 | 151 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–4 | 5 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 32–150 | 116 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 47–147 | 98 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 47–59 | 13 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 60–108 | 36 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 65–79 | 15 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 76–81 | 6 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 83–150 | 63 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 85–102 | 10 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 111–150 | 40 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 144–150 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 88 targets track ID '117', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 142: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 142: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 142: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '10' (Unknown) duration 132 frames exceeds threshold 90 frames [start=19, end=150].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (TE1) duration 132 frames exceeds threshold 90 frames [start=19, end=150].
- ⚠️ Action 'Action_None' range [16-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-59] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [41-99] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-89] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [19-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [19-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [19-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [44-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-63] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-67] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-59] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-147] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-59] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-79] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-79] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>