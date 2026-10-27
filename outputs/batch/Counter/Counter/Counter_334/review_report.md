# Play-Annotation-Generator Annotation Review — Counter_334

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_334`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `9` | `8` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | defense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 124 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `9` | `8` | 122 | START | 122 | 124 |
| ✅ EXACT | `Action_DownBlock` | RT | `13` | `12` | 125 | START | 125 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `2` | `1` | 125 | START | 125 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `7` | `6` | 125 | START | 125 | 154 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `9` | `8` | 125 | START | 125 | 177 |
| ✅ EXACT | `Action_PullLeadBlock` | DE2 | `5` | `4` | 125 | START | 125 | 245 |
| ✅ EXACT | `Action_SnapReceive` | RB | `6` | `5` | 139 | END | 122 | 139 |
| ✅ EXACT | `Action_Handoff` | RB | `6` | `5` | 149 | START | 149 | 171 |
| ✅ EXACT | `Action_BallCarry` | QB | `3` | `2` | 172 | START | 172 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 245 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 210 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_SnapReceive` | 122 | 139 | 18 | inferred_complete_timeline |
| `Action_None` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 149 | 171 | 23 | inferred_complete_timeline |
| `Action_None` | 172 | 195 | 24 | inferred_complete_timeline |
| `Action_None` | 197 | 241 | 45 | inferred_complete_timeline |
| `Action_None` | 243 | 254 | 12 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 121 | 56 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 191 | 67 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 221 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 223 | 245 | 23 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 154 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 245 | 87 | inferred_complete_timeline |
| `Action_None` | 246 | 279 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 124 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 245 | 121 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 207 | 86 | inferred_complete_timeline |
| `Action_None` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_None` | 217 | 297 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 124 | 82 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 125 | 245 | 121 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 141 | 20 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 296 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 150 | 29 | inferred_complete_timeline |
| `Action_None` | 159 | 176 | 18 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_None` | 122 | 192 | 71 | inferred_complete_timeline |
| `Action_None` | 194 | 255 | 62 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–177 | 177 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–142 | 139 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–215 | 209 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 19–20 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 166–197 | 27 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 180–262 | 83 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 195–299 | 105 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 195–299 | 105 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 201–299 | 96 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 205–246 | 39 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 210–299 | 72 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 212–299 | 88 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 226–282 | 53 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 228–251 | 17 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 244–269 | 12 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 670: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 670: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 670: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (LG) duration 121 frames exceeds threshold 90 frames [start=125, end=245].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (RG) duration 121 frames exceeds threshold 90 frames [start=125, end=245].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 121 frames exceeds threshold 90 frames [start=125, end=245].
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-296] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [125-245] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [125-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-255] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-245] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-215] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-183] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-265] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-230] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-251] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-251] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>