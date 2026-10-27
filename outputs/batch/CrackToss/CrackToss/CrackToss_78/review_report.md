# Play-Annotation-Generator Annotation Review — CrackToss_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_78`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 72
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 6
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_CrackBlock` | TE | offense | `16` | `15` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 7 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 78 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `15` | `14` | 76 | START | 76 | 87 |
| ✅ EXACT | `Action_CrackBlock` | TE | `16` | `15` | 79 | START | 79 | 148 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `4` | `3` | 79 | START | 79 | 97 |
| ✅ EXACT | `Action_PullBlock` | LT | `7` | `6` | 79 | START | 79 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 87 | END | 76 | 87 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 92 | START | 92 | 110 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `17` | `16` | 111 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_None` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_Toss` | 92 | 110 | 19 | inferred_complete_timeline |
| `Action_None` | 111 | 147 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_CrackBlock` | 79 | 148 | 70 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 148 | 70 | inferred_complete_timeline |
| `Action_None` | 149 | 225 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 75 | 69 | inferred_complete_timeline |
| `Action_None` | 76 | 107 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 161 | 86 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 225 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 189 | 114 | inferred_complete_timeline |
| `Action_None` | 192 | 225 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 119 | 44 | inferred_complete_timeline |
| `Action_None` | 121 | 225 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 124 | 49 | inferred_complete_timeline |
| `Action_None` | 126 | 213 | 88 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 141 | 66 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 225 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 162 | 87 | inferred_complete_timeline |
| `Action_None` | 164 | 225 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–97 | 98 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–223 | 216 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–225 | 226 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–225 | 197 | 6 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–225 | 225 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 43–168 | 126 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 90–147 | 49 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 102–225 | 124 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 123–225 | 76 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 149–225 | 77 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 150–225 | 76 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 153–225 | 73 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 153–197 | 45 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 163–167 | 5 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 178–225 | 48 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 211–225 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | 54 | 67 | 8 | 57.1% | 57–61, 65 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallCarry` on target `17` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 158: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=111, end=38. Clamping end to start.
- ⚠️ Action 'Action_None' range [76-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [79-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-144] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [79-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-225] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-161] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-225] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [79-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-225] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-225] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>