# Play-Annotation-Generator Annotation Review — CrackToss_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_60`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 59
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR | offense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | DE1 | defense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 17 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | DT1 | `14` | `13` | 18 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR | `13` | `12` | 21 | START | 21 | 40 |
| ✅ EXACT | `Action_PullBlock` | RT | `11` | `10` | 21 | START | 21 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 23 | END | 18 | 23 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 33 | START | 33 | 49 |
| ✅ EXACT | `Action_BallCarry` | DE1 | `2` | `1` | 50 | START | 50 | 131 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 77 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–82
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_None` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_Toss` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 82 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_CrackBlock` | 21 | 40 | 20 | inferred_complete_timeline |
| `Action_CrackBlock` | 42 | 77 | 36 | inferred_complete_timeline |
| `Action_None` | 78 | 150 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 99 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 74 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 21 | 77 | 57 | inferred_complete_timeline |
| `Action_None` | 78 | 150 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 131 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 46 | 29 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 61 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 150 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_None` | 38 | 150 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 50 | 55 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–149 | 143 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 28–150 | 123 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 35–42 | 5 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 57–150 | 94 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 61–150 | 90 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 74–150 | 77 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 76–97 | 22 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 78–150 | 58 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 94–150 | 57 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 96–150 | 53 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 111–115 | 5 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `14` (DT1)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 122: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [18-150] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-49] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-145] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-74] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-55] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [21-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-150] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-28] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-97] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-150] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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