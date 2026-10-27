# Play-Annotation-Generator Annotation Review — CrackToss_53

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 85
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | DT1 | defense | `13` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `17` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 59 | START | 59 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 61 | END | 59 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `17` | `16` | 62 | START | 62 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `18` | `17` | 62 | START | 62 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE | `19` | `18` | 62 | START | 62 | 107 |
| ✅ EXACT | `Action_Toss` | QB | `21` | `20` | 76 | START | 76 | 90 |
| ✅ EXACT | `Action_BallCarry` | DT1 | `13` | `12` | 91 | START | 91 | 151 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_Toss` | 76 | 90 | 15 | inferred_complete_timeline |
| `Action_None` | 91 | 100 | 10 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_None` | 139 | 175 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_CrackBlock` | 62 | 145 | 84 | inferred_complete_timeline |
| `Action_CrackBlock` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_CrackBlock` | 158 | 175 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 168 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 140 | 82 | inferred_complete_timeline |
| `Action_None` | 145 | 160 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 107 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 175 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 147 | 89 | inferred_complete_timeline |
| `Action_None` | 149 | 175 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 62 | 107 | 46 | inferred_complete_timeline |
| `Action_None` | 111 | 175 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 121 | 63 | inferred_complete_timeline |
| `Action_None` | 127 | 163 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_None` | 88 | 175 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 125 | 67 | inferred_complete_timeline |
| `Action_None` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 175 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 175 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 151 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 148 | 90 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 175 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 175 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 175 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 175 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 160 | 102 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 172 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–82 | 83 | 2 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–175 | 164 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–175 | 174 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 102–175 | 74 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 136–158 | 11 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 146–150 | 5 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 153–166 | 8 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 161–175 | 14 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 162–175 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 117 targets track ID '146', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 107: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 108: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (Unknown) duration 114 frames exceeds threshold 90 frames [start=62, end=175].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '18' (TE) duration 114 frames exceeds threshold 90 frames [start=62, end=175].
- ⚠️ Action 'Action_None' range [59-140] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-119] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-175] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [62-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [148-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [158-175] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [116-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [110-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-100] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-137] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-175] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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