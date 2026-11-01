# Play-Annotation-Generator Annotation Review — InsideZoneRead_288

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_288`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 71 | START | 71 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 74 | START | 74 | 133 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 74 | START | 80 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 74 | START | 74 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `2` | 74 | START | 74 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 74 | START | 74 | 119 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 79 | END | 71 | 79 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 86 | START | 86 | 93 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 94 | START | 94 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `11` | 122 | START | 122 | 167 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_SnapReceive` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_Keep` | 94 | 121 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 167 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 233 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 248 | 267 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 128 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 133 | 60 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 119 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BallSnap` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 133 | 54 | inferred_complete_timeline |
| `Action_None` | 134 | 163 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 112 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 133 | 20 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 133 | 60 | inferred_complete_timeline |
| `Action_None` | 134 | 157 | 24 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 269 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 102 | 32 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 95 | 25 | inferred_complete_timeline |
| `Action_None` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_None` | 121 | 182 | 62 | inferred_complete_timeline |
| `Action_None` | 187 | 231 | 45 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_None` | 71 | 169 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 82–90 | 7 | 2 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 112–139 | 25 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 123–253 | 72 | 3 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 130–232 | 99 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 132–269 | 138 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 141–245 | 80 | 6 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 150–268 | 108 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 159–269 | 109 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 164–228 | 65 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 173–188 | 13 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 179–191 | 11 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 185–269 | 77 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 191–269 | 79 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 193–269 | 73 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 193–237 | 45 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 226–269 | 44 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 234–269 | 36 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 249–269 | 17 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 256–257 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 260–264 | 4 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 74 != Inferred start 80
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [71–79], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=80.
- ⚠️ Action 'Action_None' range [134-157] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-269] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-128] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-231] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [122-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-233] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-267] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-232] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-207] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-252] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-263] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>