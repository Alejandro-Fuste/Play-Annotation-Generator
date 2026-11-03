# Play-Annotation-Generator Annotation Review — Post10to15_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_45`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 108
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunPostRoute` | LB3 | defense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 8 | START | 8 | 23 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `10` | `10` | 11 | START | 24 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 11 | START | 11 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 11 | START | 11 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 11 | START | 11 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 11 | START | 11 | 49 |
| ✅ EXACT | `Action_RunPostRoute` | LB3 | `1` | `1` | 23 | START | 23 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 23 | END | 8 | 23 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 68 | START | 68 | 73 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 23 | 16 | inferred_complete_timeline |
| `Action_None` | 24 | 67 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 74 | 111 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 66 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 49 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 82 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 150 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 23 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 35 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 57 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 122 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 66 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 74 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 72 | 81 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunPostRoute` | 23 | 66 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 49 | 150 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 150 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 123 | 116 | inferred_complete_timeline |
| `Action_None` | 125 | 150 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 44–81 | 26 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 67–125 | 59 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 70–150 | 29 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 70–150 | 81 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 71–74 | 4 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 71–150 | 19 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 75–101 | 12 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 94–97 | 4 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 97–110 | 11 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 123–145 | 7 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 133–150 | 16 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 139–150 | 5 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 140–150 | 11 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 141–150 | 10 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 141–150 | 9 | 2 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 141–148 | 7 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `10` (C): Annotated start 11 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [8–23], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [8-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [23-66] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-35] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-150] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-81] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-125] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-78] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-78] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-81] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-104] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>