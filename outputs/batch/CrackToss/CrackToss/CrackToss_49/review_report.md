# Play-Annotation-Generator Annotation Review — CrackToss_49

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 95
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | TE2 | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | LT | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 78 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `21` | `18` | 79 | START | 88 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 81 | END | 79 | 81 |
| ✅ EXACT | `Action_CrackBlock` | TE2 | `11` | `10` | 82 | START | 82 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `18` | `17` | 82 | START | 82 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `3` | `2` | 82 | START | 82 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | QB | `12` | `11` | 97 | START | 97 | 108 |
| ✅ EXACT | `Action_BallCarry` | LT | `5` | `4` | 113 | START | 113 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_Toss` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_Toss` | 112 | 112 | 1 | inferred_complete_timeline |
| `Action_None` | 113 | 157 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 97 | 136 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_CrackBlock` | 82 | 105 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 185 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 96 | 18 | inferred_complete_timeline |
| `Action_None` | 99 | 114 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–9
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 9 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 153 | 75 | inferred_complete_timeline |
| `Action_None` | 155 | 195 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 94 | 16 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 145 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 111 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 152 | 74 | inferred_complete_timeline |
| `Action_None` | 155 | 194 | 40 | inferred_complete_timeline |
| `Action_None` | 199 | 225 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 138 | 60 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 225 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–200 | 198 | 4 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–150 | 151 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–140 | 139 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 63–225 | 159 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 88–225 | 138 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 105–118 | 10 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 116–207 | 92 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 116–179 | 39 | 7 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 123–160 | 29 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 127–153 | 27 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 129–225 | 87 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 130–149 | 16 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 157–202 | 42 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 193–197 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `21` (Position_Unknown): Annotated start 79 != Inferred start 88
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 135 targets track ID '168', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 99: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (Unknown) duration 119 frames exceeds threshold 90 frames [start=82, end=200].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (Unknown) duration 144 frames exceeds threshold 90 frames [start=82, end=225].
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=88, end=81. Clamping end to start.
- ⚠️ Action 'Action_None' range [79-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-194] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-155] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [158-183] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [185-200] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-195] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [82-105] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [97-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-155] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [160-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-225] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-207] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-160] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-191] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-202] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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