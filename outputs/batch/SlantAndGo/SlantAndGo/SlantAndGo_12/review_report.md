# Play-Annotation-Generator Annotation Review — SlantAndGo_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_12`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_SellRoute` | SAF | defense | `16` | `15` |
| ✅ EXACT | `Action_VerticalStem` | SAF | defense | `16` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 10 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RG | `11` | `11` | 8 | START | N/A | N/A |
| ✅ EXACT | `Action_PassBlock` | RT | `0` | `0` | 11 | START | 11 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `11` | `11` | 11 | START | 11 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `6` | `6` | 11 | START | 11 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `8` | 11 | START | 11 | 52 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 22 | END | 8 | 22 |
| ✅ EXACT | `Action_SellRoute` | SAF | `16` | `15` | 49 | START | 49 | 69 |
| ✅ EXACT | `Action_VerticalStem` | SAF | `16` | `15` | 70 | START | 70 | 125 |
| ✅ EXACT | `Action_ThrowPass` | QB | `1` | `1` | 98 | START | 98 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 22 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 97 | 75 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 153 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 113 | 106 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 165 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 57 | 50 | inferred_complete_timeline |
| `Action_None` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_None` | 103 | 156 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 24 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 38 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 14 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 151 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 140 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 30 | 23 | inferred_complete_timeline |
| `Action_None` | 39 | 74 | 36 | inferred_complete_timeline |
| `Action_None` | 77 | 103 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 13 | 6 | inferred_complete_timeline |
| `Action_None` | 25 | 32 | 8 | inferred_complete_timeline |
| `Action_None` | 35 | 50 | 16 | inferred_complete_timeline |
| `Action_None` | 67 | 84 | 18 | inferred_complete_timeline |
| `Action_None` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 109 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 50 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 131 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 49–125
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SellRoute` | 49 | 69 | 21 | inferred_complete_timeline |
| `Action_VerticalStem` | 70 | 125 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–210 | 203 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–149 | 146 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–210 | 180 | 6 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 47–159 | 113 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 54–121 | 68 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 56–201 | 119 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 104–116 | 13 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 119–204 | 86 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 124–198 | 75 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 126–145 | 20 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 130–178 | 46 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 136–151 | 15 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 190–210 | 20 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `11` (RG)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 22: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 22: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PassBlock' range [11-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-113] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-57] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-30] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-24] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-13] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-32] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-129] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-159] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [70-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-178] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>