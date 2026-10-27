# Play-Annotation-Generator Annotation Review — Dagger_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_31`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 3
- **Action Segments:** 48
- **Validation Warnings:** 104
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
- **Inferred Coverage Segments (Action_None):** 48
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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–326 | 326 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–318 | 319 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–329 | 324 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–265 | 266 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–318 | 319 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–323 | 323 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–329 | 329 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–329 | 283 | 5 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–52 | 53 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–237 | 238 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–47 | 48 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–246 | 246 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–323 | 324 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–322 | 309 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–327 | 326 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–256 | 252 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 2–299 | 298 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 119–144 | 24 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 226–228 | 3 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 250–328 | 78 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 270–293 | 24 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 303–321 | 19 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 304–319 | 16 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 312–329 | 18 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 313–329 | 17 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | 121 | 163 | 33 | 76.7% | 127, 134, 143–145, 147, 154, 160–162 |
| `22` | `29` | 229 | 238 | 9 | 90.0% | 236 |
| `23` | `33` | 247 | 274 | 16 | 57.1% | 250, 253, 255–264 |

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
| Missing visible bounding boxes during action | 40 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-326] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-318] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-318] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-323] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-290] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-246] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-128] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-236] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-322] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-327] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-144] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-328] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-293] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-321] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-319] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>