# Play-Annotation-Generator Annotation Review — Dagger_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_47`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 268
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 52
- **Validation Warnings:** 102
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
- **Inferred Coverage Segments (Action_None):** 52
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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–14 | 15 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–268 | 269 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 5–14 | 10 | 1 | Undefined position; Undefined team |
| `7` | `10` | Position_Unknown | Team_Unknown | 13–268 | 254 | 3 | Undefined position; Undefined team |
| `8` | `11` | Position_Unknown | Team_Unknown | 14–268 | 251 | 2 | Undefined position; Undefined team |
| `9` | `12` | Position_Unknown | Team_Unknown | 14–254 | 241 | 1 | Undefined position; Undefined team |
| `10` | `13` | Position_Unknown | Team_Unknown | 14–268 | 255 | 1 | Undefined position; Undefined team |
| `11` | `14` | Position_Unknown | Team_Unknown | 14–216 | 203 | 1 | Undefined position; Undefined team |
| `12` | `15` | Position_Unknown | Team_Unknown | 14–268 | 255 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 14–268 | 238 | 6 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 14–268 | 255 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 14–190 | 177 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 14–268 | 251 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 14–268 | 165 | 8 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 14–261 | 248 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 14–177 | 164 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 14–268 | 255 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 128–199 | 66 | 5 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 171–268 | 97 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 204–219 | 11 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 242–268 | 27 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 256–267 | 12 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 257–259 | 3 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 268–268 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 42 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-14] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-218] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-235] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-254] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-237] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-94] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-165] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-261] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-268] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-172] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-244] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '27' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>