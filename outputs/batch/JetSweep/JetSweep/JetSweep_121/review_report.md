# Play-Annotation-Generator Annotation Review — JetSweep_121

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_121`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `14` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | LB1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 88 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 89 | START | 89 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 91 | START | 91 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 91 | START | 91 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `12` | 91 | START | 91 | 190 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `14` | `13` | 91 | START | N/A | N/A |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `15` | `14` | 98 | START | 98 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 103 | END | 89 | 103 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 108 | START | 108 | 118 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `15` | `14` | 119 | START | 123 | 152 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | LB1 | `7` | `6` | 120 | START | 133 | 193 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_Toss` | 108 | 118 | 11 | inferred_complete_timeline |
| `Action_None` | 119 | 132 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 124 | 36 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 149 | 18 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 189 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 91 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 190 | 100 | inferred_complete_timeline |
| `Action_None` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 133 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 193 | 59 | inferred_complete_timeline |
| `Action_None` | 194 | 267 | 74 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 115 | 27 | inferred_complete_timeline |
| `Action_None` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_None` | 133 | 145 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 181 | 93 | inferred_complete_timeline |
| `Action_None` | 207 | 268 | 62 | inferred_complete_timeline |
| `Action_None` | 270 | 274 | 5 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 180 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 105 | 17 | inferred_complete_timeline |
| `Action_None` | 126 | 138 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 116 | 46 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 133 | 193 | 61 | inferred_complete_timeline |
| `Action_None` | 194 | 211 | 18 | inferred_complete_timeline |
| `Action_None` | 217 | 279 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_None` | 167 | 191 | 25 | inferred_complete_timeline |
| `Action_None` | 199 | 250 | 52 | inferred_complete_timeline |
| `Action_None` | 252 | 263 | 12 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 88 | 51 | inferred_complete_timeline |
| `Action_None` | 89 | 263 | 175 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_None` | 89 | 138 | 50 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 88–152 | 61 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 101–299 | 197 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 114–246 | 61 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 136–153 | 18 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 137–299 | 153 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 156–226 | 59 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 184–299 | 109 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 184–199 | 16 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 225–299 | 75 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 227–299 | 73 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 227–299 | 68 | 5 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 232–296 | 61 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 234–261 | 21 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 237–296 | 51 | 3 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 256–260 | 5 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 283–288 | 5 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (C)
- ⚠️ `Action_BallCarry` for actor_track_id `15` (Position_Unknown): Annotated start 119 != Inferred start 123
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `7` (LB1): Annotated start 120 != Inferred start 133

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 244: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 103 frames exceeds threshold 90 frames [start=91, end=193].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 99 frames exceeds threshold 90 frames [start=91, end=189].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RG) duration 103 frames exceeds threshold 90 frames [start=91, end=193].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [89–91], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=92.
- ⚠️ Action 'Action_ZoneBlock' range [91-133] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-181] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-124] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-116] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-190] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [89-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [98-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-230] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-126] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-191] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-274] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>