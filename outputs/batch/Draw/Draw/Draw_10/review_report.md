# Play-Annotation-Generator Annotation Review — Draw_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_10`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `9` | `8` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | RB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `10` | `9` | 40 | START | 40 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `11` | 43 | START | 43 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `3` | 43 | START | 43 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `7` | 43 | START | 43 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `9` | `8` | 43 | START | 43 | 88 |
| ⚠️ END CHANGED | `Action_SnapReceive` | RB | `6` | `5` | 54 | END | 40 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | RB | `6` | `5` | 58 | START | 58 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 86 | START | 88 | 109 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 123 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_None` | 52 | 71 | 20 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 120 | 40 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 53 | 14 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 58 | 64 | 7 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 71 | 84 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 109 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 115 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 112 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 74 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 123 | 34 | inferred_complete_timeline |
| `Action_None` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 88 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 123 | 33 | inferred_complete_timeline |
| `Action_None` | 124 | 210 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 123 | 81 | inferred_complete_timeline |
| `Action_None` | 124 | 163 | 40 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 39 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_None` | 55 | 55 | 1 | inferred_complete_timeline |
| `Action_None` | 63 | 82 | 20 | inferred_complete_timeline |
| `Action_None` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_None` | 104 | 146 | 43 | inferred_complete_timeline |
| `Action_None` | 148 | 163 | 16 | inferred_complete_timeline |
| `Action_None` | 168 | 210 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 80 | 41 | inferred_complete_timeline |
| `Action_None` | 86 | 101 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 97 | 58 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–104 | 97 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 2–4 | 3 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 54–186 | 79 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 97–210 | 111 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 120–210 | 91 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 126–210 | 77 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 135–210 | 75 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 141–210 | 55 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 192–210 | 19 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 192–210 | 19 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 197–201 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_FakePassDroptoHandoff` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 22: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [40-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [40-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [58-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [67-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [71-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 55, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [55-55] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-118] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-154] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>