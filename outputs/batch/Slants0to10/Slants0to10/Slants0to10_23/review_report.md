# Play-Annotation-Generator Annotation Review — Slants0to10_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 5 | START | 5 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 5 | START | 5 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 5 | START | 5 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 5 | START | 5 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 5 | START | 5 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 5 | START | 5 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 5 | START | 5 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 5 | START | 5 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 5 | START | 5 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 5 | START | 5 | 8 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 9 | START | 9 | 18 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | RT | `15` | `15` | 17 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 17 | START | 17 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 17 | START | 33 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 17 | START | 17 | 29 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 17 | START | 17 | 210 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `7` | `7` | 23 | START | 23 | 77 |
| ✅ EXACT | `Action_SnapReceive` | RT | `15` | `15` | 23 | END | 9 | 23 |
| ✅ EXACT | `Action_ThrowPass` | RT | `15` | `15` | 70 | START | 70 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `7` | `7` | 112 | START | 112 | 139 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–43
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 43 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 22 | 18 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 23 | 77 | 55 | inferred_complete_timeline |
| `Action_None` | 78 | 111 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 139 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 180 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 194 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 5–93
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 61 | 53 | inferred_complete_timeline |
| `Action_None` | 64 | 80 | 17 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–73
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 38 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 62 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 73 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 18 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–142
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 23 | 15 | inferred_complete_timeline |
| `Action_None` | 24 | 69 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_None` | 78 | 137 | 60 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 92 | 84 | inferred_complete_timeline |
| `Action_None` | 94 | 101 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 210 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 85 | 77 | inferred_complete_timeline |
| `Action_None` | 88 | 122 | 35 | inferred_complete_timeline |
| `Action_None` | 126 | 210 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–167
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 70 | 62 | inferred_complete_timeline |
| `Action_None` | 78 | 167 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 135 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–171
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 86 | 78 | inferred_complete_timeline |
| `Action_None` | 88 | 171 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–126
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 8 | 4 | inferred_complete_timeline |
| `Action_None` | 9 | 126 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 5–140 | 129 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 45–157 | 45 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 50–210 | 149 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 74–85 | 6 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 84–210 | 127 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 133–210 | 55 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 164–166 | 3 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 189–206 | 15 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `15` (RT)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 23: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '15' has invalid range: start=17, end=8. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [9–23], lower_priority='Action_PassBlock' annotated_start=17, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [9-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-85] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-171] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-167] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-137] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [9-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [17-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>