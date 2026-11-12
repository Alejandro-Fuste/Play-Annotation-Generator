# Play-Annotation-Generator Annotation Review — SplitZone_118

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_118`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 91 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 89 | START | 89 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 92 | START | 92 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 92 | START | 105 | 169 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 92 | START | 92 | 190 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 92 | START | 92 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 92 | START | 92 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `14` | `14` | 93 | START | 93 | 177 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 104 | END | 89 | 104 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 114 | START | 114 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 128 | START | 128 | 132 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_None` | 128 | 182 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 275 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 141 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 156 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 193 | 36 | inferred_complete_timeline |
| `Action_None` | 194 | 239 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 169 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 193 | 11 | inferred_complete_timeline |
| `Action_None` | 194 | 249 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 190 | 99 | inferred_complete_timeline |
| `Action_None` | 199 | 299 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 193 | 102 | inferred_complete_timeline |
| `Action_None` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 78 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 299 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 106 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 170 | 82 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 237 | 149 | inferred_complete_timeline |
| `Action_None` | 239 | 299 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 229 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 31–222 | 191 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 45–299 | 255 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 105–208 | 102 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 146–181 | 30 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 179–299 | 121 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 184–199 | 6 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 193–299 | 107 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 200–234 | 26 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 214–248 | 33 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 240–299 | 60 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 244–287 | 44 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 277–281 | 5 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 282–299 | 5 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 283–289 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 102 frames exceeds threshold 90 frames [start=92, end=193].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 102 frames exceeds threshold 90 frames [start=92, end=193].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 102 frames exceeds threshold 90 frames [start=92, end=193].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 102 frames exceeds threshold 90 frames [start=92, end=193].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [89–104], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=105.
- ⚠️ Action 'Action_None' range [89-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-190] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-275] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-249] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-170] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [93-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-204] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-248] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-287] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '31' has 3 frames without a visible bounding box.
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