# Play-Annotation-Generator Annotation Review — Counter_140

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_140`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 52 | START | 52 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `1` | `0` | 56 | START | 56 | 89 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `11` | `10` | 56 | START | 67 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `9` | `8` | 56 | START | 56 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 56 | START | 56 | 69 |
| ✅ EXACT | `Action_SnapReceive` | RB | `6` | `5` | 66 | END | 52 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 82 | START | 82 | 192 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 172 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 52 | 66 | 15 | inferred_complete_timeline |
| `Action_None` | 67 | 81 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 192 | 111 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 56 | 69 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 93 | 110 | 18 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 122 | 159 | 38 | inferred_complete_timeline |
| `Action_None` | 160 | 230 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 56 | 89 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 159 | 53 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 170 | 191 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 85 | 34 | inferred_complete_timeline |
| `Action_None` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 239 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_BallSnap` | 52 | 66 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 67 | 159 | 93 | inferred_complete_timeline |
| `Action_None` | 160 | 191 | 32 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 138 | 87 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 202 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 152 | 101 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 203 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 75 | 24 | inferred_complete_timeline |
| `Action_None` | 77 | 202 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 74 | 23 | inferred_complete_timeline |
| `Action_None` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 124 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 162 | 111 | inferred_complete_timeline |
| `Action_None` | 178 | 239 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 194 | 143 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–239 | 220 | 10 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 47–122 | 75 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 86–205 | 120 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 110–211 | 83 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 117–154 | 38 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 143–239 | 97 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 153–239 | 87 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 161–220 | 60 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 164–172 | 9 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 167–233 | 66 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 171–207 | 19 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 172–183 | 7 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 184–239 | 56 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 213–239 | 24 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 216–239 | 20 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 225–239 | 13 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `11` (C): Annotated start 56 != Inferred start 67
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 282: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 282: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (LT) duration 104 frames exceeds threshold 90 frames [start=56, end=159].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (Unknown) duration 104 frames exceeds threshold 90 frames [start=56, end=159].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (C) duration 104 frames exceeds threshold 90 frames [start=56, end=159].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [52–66], lower_priority='Action_DownBlock' annotated_start=56, effective_Action_DownBlock_start=67.
- ⚠️ Action 'Action_DownBlock' range [56-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-138] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [56-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [72-76] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [93-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [117-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-194] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-202] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-124] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [56-70] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [76-96] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [122-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [67-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-205] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-173] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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