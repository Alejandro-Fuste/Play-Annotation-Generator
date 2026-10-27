# Play-Annotation-Generator Annotation Review — Dagger_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_13`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 28
- **Ball Tracks:** 2
- **Action Segments:** 58
- **Validation Warnings:** 110
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
- **Inferred Coverage Segments (Action_None):** 58
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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–315 | 311 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–178 | 179 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–149 | 150 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–212 | 213 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–233 | 227 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–286 | 287 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–303 | 302 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–216 | 217 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–279 | 278 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–266 | 264 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–295 | 250 | 4 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–253 | 167 | 6 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–306 | 301 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–185 | 186 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–329 | 315 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–147 | 143 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 151–290 | 140 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 158–291 | 134 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 159–288 | 126 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 251–329 | 72 | 5 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 255–329 | 75 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 258–329 | 62 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 279–325 | 46 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 282–329 | 48 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 0 | 70 | 44 | 62.0% | 26–28, 30, 39–40, 42–46, 52–65, 68–69 |
| `21` | `26` | 211 | 214 | 4 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 52 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-301] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-286] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-303] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-279] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-266] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-246] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-306] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-329] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-290] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-288] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-267] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-295] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-300] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-314] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-325] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>