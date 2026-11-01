# Play-Annotation-Generator Annotation Review — InsideZoneRead_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_22`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 55 | START | 55 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 57 | START | 57 | 154 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `10` | 57 | START | 70 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 57 | START | 57 | 154 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `2` | 57 | START | 57 | 154 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 57 | START | 57 | 154 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 69 | END | 55 | 69 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 73 | START | 73 | 80 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 81 | START | 81 | 94 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 95 | START | 95 | 157 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 154 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 95 | 157 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 154 | 98 | inferred_complete_timeline |
| `Action_None` | 155 | 177 | 23 | inferred_complete_timeline |
| `Action_None` | 183 | 197 | 15 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 269 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 154 | 98 | inferred_complete_timeline |
| `Action_None` | 155 | 171 | 17 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 154 | 85 | inferred_complete_timeline |
| `Action_None` | 155 | 206 | 52 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 154 | 98 | inferred_complete_timeline |
| `Action_None` | 155 | 191 | 37 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 154 | 98 | inferred_complete_timeline |
| `Action_None` | 155 | 218 | 64 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 116 | 62 | inferred_complete_timeline |
| `Action_None` | 128 | 146 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 94 | 40 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 124 | 20 | inferred_complete_timeline |
| `Action_None` | 143 | 205 | 63 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 78 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 59 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 77 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 254 | 200 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 177 | 123 | inferred_complete_timeline |
| `Action_None` | 179 | 186 | 8 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–15
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 76–103 | 25 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 92–133 | 37 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 101–269 | 167 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 118–269 | 113 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 124–269 | 146 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 127–269 | 143 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 131–269 | 139 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 134–269 | 126 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 139–142 | 4 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 147–269 | 115 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 151–269 | 119 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 157–268 | 106 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 159–269 | 110 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 160–203 | 44 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 180–234 | 15 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 201–269 | 68 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 212–219 | 8 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 235–261 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 57 != Inferred start 70
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RG) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [55–69], lower_priority='Action_ZoneBlock' annotated_start=57, effective_Action_ZoneBlock_start=70.
- ⚠️ Action 'Action_ZoneBlock' range [57-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [95-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-124] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-205] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-254] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-244] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-249] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-249] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-246] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-261] for track '32' has 1 frames without a visible bounding box.
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

</details>