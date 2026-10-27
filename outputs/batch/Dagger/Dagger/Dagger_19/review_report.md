# Play-Annotation-Generator Annotation Review — Dagger_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_19`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 123
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
- **Inferred Coverage Segments (Action_None):** 65
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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–126 | 127 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–254 | 255 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–254 | 255 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–247 | 248 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–264 | 247 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–165 | 165 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–299 | 294 | 4 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–237 | 238 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–299 | 300 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–166 | 152 | 6 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–196 | 197 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–136 | 137 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–222 | 216 | 4 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–250 | 250 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–169 | 170 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–143 | 138 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 2–122 | 67 | 7 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 20–38 | 9 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 54–143 | 19 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 99–296 | 197 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 140–250 | 110 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 146–291 | 146 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 174–299 | 117 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 185–256 | 71 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 212–295 | 83 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 218–299 | 82 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 224–299 | 65 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 225–299 | 75 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 226–299 | 74 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 240–242 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 263–268 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 59 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-51] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-114] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-250] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-4] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-83] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-143] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-296] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-209] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-189] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-256] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-295] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-290] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-268] for track '30' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>