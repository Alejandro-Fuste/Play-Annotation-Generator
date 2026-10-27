# Play-Annotation-Generator Annotation Review — Counter_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_22`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | RB1 | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | RB1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | defense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB1 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 39 | START | 39 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `12` | `11` | 42 | START | 42 | 121 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `15` | `14` | 42 | START | 60 | 78 |
| ✅ EXACT | `Action_DownBlock` | RB1 | `3` | `2` | 42 | START | 42 | 90 |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | RB1 | `3` | `2` | 42 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `14` | `13` | 42 | START | 42 | 60 |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | `10` | `9` | 42 | START | 42 | 154 |
| ✅ EXACT | `Action_SnapReceive` | SAF1 | `5` | `4` | 55 | END | 39 | 55 |
| ✅ EXACT | `Action_Handoff` | C | `15` | `14` | 79 | START | 79 | 90 |
| ✅ EXACT | `Action_BallCarry` | RB1 | `3` | `2` | 91 | START | 91 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 154 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 129 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 42 | 90 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 42 | 154 | 113 | inferred_complete_timeline |
| `Action_None` | 155 | 210 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 42 | 121 | 80 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 154 | 31 | inferred_complete_timeline |
| `Action_None` | 155 | 166 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PullBlock` | 42 | 60 | 19 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 75 | 147 | 73 | inferred_complete_timeline |
| `Action_PullBlock` | 149 | 151 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 91 | 168 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 86 | 48 | inferred_complete_timeline |
| `Action_None` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 206 | 168 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 164 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 147 | 109 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_None` | 170 | 176 | 7 | inferred_complete_timeline |
| `Action_None` | 182 | 195 | 14 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 82 | 44 | inferred_complete_timeline |
| `Action_None` | 86 | 140 | 55 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 210 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 79 | 41 | inferred_complete_timeline |
| `Action_None` | 82 | 121 | 40 | inferred_complete_timeline |
| `Action_None` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 188 | 150 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 92–195 | 102 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 166–209 | 43 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 196–210 | 15 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (C): Annotated start 42 != Inferred start 60
- ❌ Missing segment for action `Action_PlaySideFakeStep` on target `3` (RB1)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 42 for track '2': 'Action_PlaySideFakeStep' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (TE) duration 113 frames exceeds threshold 90 frames [start=42, end=154].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '13' (LG) duration 110 frames exceeds threshold 90 frames [start=42, end=151].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [39–55], lower_priority='Action_DownBlock' annotated_start=42, effective_Action_DownBlock_start=56.
- ⚠️ Action 'Action_None' range [39-188] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [42-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [42-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [65-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [75-147] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [149-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [39-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-86] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-103] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '27' has 1 frames without a visible bounding box.
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