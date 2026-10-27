# Play-Annotation-Generator Annotation Review — Dagger_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_29`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 56
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
- **Inferred Coverage Segments (Action_None):** 56
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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–249 | 248 | 3 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–241 | 241 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–246 | 247 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–181 | 182 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–173 | 174 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–234 | 232 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–186 | 187 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–235 | 234 | 3 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–190 | 187 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–274 | 275 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–224 | 225 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–190 | 191 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–234 | 201 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–240 | 241 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–208 | 202 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 116–243 | 96 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 117–160 | 43 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 130–203 | 21 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 135–137 | 3 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 161–329 | 162 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 178–226 | 43 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 178–329 | 152 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 196–242 | 43 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 197–199 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 205–253 | 42 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 218–246 | 29 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 221–223 | 3 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 236–272 | 37 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 312–329 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 52 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-237] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-249] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-234] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-234] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-243] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-203] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-191] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-246] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>