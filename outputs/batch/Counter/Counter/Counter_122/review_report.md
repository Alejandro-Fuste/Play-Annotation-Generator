# Play-Annotation-Generator Annotation Review — Counter_122

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_122`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 98
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | SAF2 | defense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `12` | `11` | 48 | START | 48 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | `11` | `10` | 53 | START | 53 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `12` | `11` | 53 | START | 53 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `7` | `6` | 53 | START | 53 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `14` | `13` | 53 | START | 53 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 61 | END | 48 | 61 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 70 | START | 70 | 86 |
| ✅ EXACT | `Action_BallCarry` | SAF2 | `13` | `12` | 93 | START | 93 | 143 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_None` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 70 | 86 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 72 | 25 | inferred_complete_timeline |
| `Action_None` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 53 | 98 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 47 | 38 | inferred_complete_timeline |
| `Action_None` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_None` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_None` | 80 | 84 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PullBlock` | 53 | 73 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 119 | 130 | 12 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 67 | 20 | inferred_complete_timeline |
| `Action_None` | 107 | 140 | 34 | inferred_complete_timeline |
| `Action_None` | 144 | 175 | 32 | inferred_complete_timeline |
| `Action_None` | 181 | 212 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 97 | 50 | inferred_complete_timeline |
| `Action_None` | 115 | 165 | 51 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 205 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 53 | 85 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 87 | 121 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 136 | 89 | inferred_complete_timeline |
| `Action_None` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_None` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 121 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_DownBlock` | 53 | 128 | 76 | inferred_complete_timeline |
| `Action_None` | 140 | 239 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 143 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–239 | 237 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–239 | 199 | 8 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 77–191 | 110 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 90–239 | 140 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 91–142 | 41 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 93–119 | 27 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 93–204 | 111 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 95–98 | 4 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 101–203 | 103 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 112–201 | 90 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 128–226 | 99 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 133–161 | 29 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 145–239 | 89 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 147–176 | 30 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 160–181 | 16 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 189–191 | 3 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `34` | `41` | 215 | 215 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 246: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 246: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 246: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [48-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-165] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [70-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [53-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [98-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [106-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [119-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-72] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-239] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [53-128] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [53-85] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [87-121] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [93-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [53-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [104-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-118] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-188] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-231] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-188] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-203] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-161] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-172] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>