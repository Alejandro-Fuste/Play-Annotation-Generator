# Play-Annotation-Generator Annotation Review — Dagger_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_35`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 2
- **Action Segments:** 60
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 0
- **Exact Matches:** 0
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–91 | 92 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 211 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–166 | 148 | 4 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–82 | 83 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–210 | 211 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–84 | 85 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–95 | 96 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–175 | 170 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–79 | 80 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–185 | 157 | 6 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–186 | 140 | 5 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–116 | 68 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–190 | 172 | 7 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–165 | 155 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–143 | 143 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–210 | 211 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–210 | 184 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–169 | 167 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–181 | 175 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 92–120 | 29 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 117–210 | 94 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 161–210 | 43 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 169–208 | 40 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 172–205 | 31 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 201–210 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | 0 | 11 | 3 | 25.0% | 1–4, 6–10 |
| `21` | `22` | 94 | 95 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 60 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-175] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-169] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-186] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-116] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-184] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-157] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-52] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-208] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>