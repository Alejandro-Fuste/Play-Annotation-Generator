# Play-Annotation-Generator Annotation Review — Post10to15_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_1`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 4 | START | 4 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 7 | START | 7 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 7 | START | 40 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `19` | `19` | 7 | START | 7 | 28 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 7 | START | 7 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 7 | START | 7 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | Position_Unknown | `15` | `15` | 21 | START | 21 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 21 | END | 4 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 59 | START | 59 | 64 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 21 | 18 | inferred_complete_timeline |
| `Action_None` | 22 | 58 | 37 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_None` | 65 | 150 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 68 | 65 | inferred_complete_timeline |
| `Action_None` | 72 | 150 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 41 | 38 | inferred_complete_timeline |
| `Action_None` | 43 | 150 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 28 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 150 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 14 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 39 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 18 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 84 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 129 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 150 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 59 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 93 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 150 | 144 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 46 | 150 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 53 | 50 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 100 | 97 | inferred_complete_timeline |
| `Action_None` | 103 | 150 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 77 | 74 | inferred_complete_timeline |
| `Action_None` | 81 | 150 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 150 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–137 | 130 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 73–150 | 78 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 80–82 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 110–150 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `15` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 3: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [4–21], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=22.
- ⚠️ Action 'Action_None' range [4-41] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-150] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-38] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-150] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [21-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [104-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [127-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [134-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-39] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [4-18] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-84] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-129] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-93] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-150] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>