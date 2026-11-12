# Play-Annotation-Generator Annotation Review — SplitZone_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_86`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 0 | START | 0 | 127 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 119 | START | 119 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 122 | START | 122 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 122 | START | 122 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 122 | START | 122 | 194 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `5` | 122 | START | 132 | 224 |
| ✅ EXACT | `Action_SplitBlock` | HB | `9` | `9` | 128 | START | 128 | 224 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 131 | END | 119 | 131 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 142 | START | 142 | 152 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `3` | 153 | START | 153 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 229 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_SplitBlock` | 128 | 224 | 97 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 194 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 167 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 224 | 55 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 119 | 131 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 224 | 93 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 147 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 173 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 224 | 50 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 299 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 140 | 22 | inferred_complete_timeline |
| `Action_None` | 151 | 170 | 20 | inferred_complete_timeline |
| `Action_None` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 234 | 41 | inferred_complete_timeline |
| `Action_None` | 237 | 285 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 299 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 217 | 99 | inferred_complete_timeline |
| `Action_None` | 219 | 273 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 232 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 118 | 22 | inferred_complete_timeline |
| `Action_None` | 119 | 268 | 150 | inferred_complete_timeline |
| `Action_None` | 270 | 293 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 9–174 | 71 | 8 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 59–227 | 169 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 66–257 | 192 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 173–299 | 127 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 185–299 | 113 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 187–190 | 4 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 203–299 | 96 | 2 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 216–299 | 84 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 218–259 | 30 | 2 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 223–299 | 77 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 233–299 | 67 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 249–252 | 4 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 254–293 | 27 | 2 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 269–273 | 5 | 1 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 122 != Inferred start 132

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 174: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 103 frames exceeds threshold 90 frames [start=122, end=224].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [119–131], lower_priority='Action_ZoneBlock' annotated_start=122, effective_Action_ZoneBlock_start=132.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 103 frames exceeds threshold 90 frames [start=122, end=224].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RG) duration 103 frames exceeds threshold 90 frames [start=122, end=224].
- ⚠️ Action 'Action_None' range [119-217] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-170] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-188] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-224] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-293] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-147] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-173] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-42] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-130] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-227] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-219] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-263] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-293] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-273] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '29' has 1 frames without a visible bounding box.
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

</details>