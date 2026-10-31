# Play-Annotation-Generator Annotation Review — Hitch_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_1`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_RunHitchRoute` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 11 | START | 11 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `1` | `1` | 14 | START | 14 | 97 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `14` | `14` | 14 | START | 26 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `2` | `2` | 14 | START | 14 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 14 | START | 14 | 251 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 25 | END | 11 | 25 |
| ✅ EXACT | `Action_RunHitchRoute` | Position_Unknown | `17` | `16` | 29 | START | 29 | 111 |
| ✅ EXACT | `Action_ThrowPass` | QB | `10` | `10` | 74 | START | 74 | 83 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `17` | `16` | 112 | START | 112 | 253 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 73 | 48 | inferred_complete_timeline |
| `Action_ThrowPass` | 74 | 83 | 10 | inferred_complete_timeline |
| `Action_None` | 84 | 125 | 42 | inferred_complete_timeline |
| `Action_None` | 131 | 215 | 85 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 113 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 114 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 97 | 84 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 144 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 165 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 269 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 143 | 130 | inferred_complete_timeline |
| `Action_PassBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 159 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 251 | 238 | inferred_complete_timeline |
| `Action_PassBlock` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 38 | 28 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 140 | 93 | inferred_complete_timeline |
| `Action_None` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 16 | 6 | inferred_complete_timeline |
| `Action_None` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 28 | 18 | inferred_complete_timeline |
| `Action_None` | 31 | 62 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 22 | 12 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 31 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 49 | 39 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 123 | 113 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 131 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 90 | 80 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 26–253 | 228 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 33–269 | 199 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 37–269 | 209 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 42–268 | 211 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 64–269 | 196 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 81–84 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 93–269 | 160 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 98–146 | 23 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 106–269 | 164 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 120–269 | 136 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 129–269 | 137 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 134–269 | 136 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 150–234 | 81 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 160–269 | 110 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 165–210 | 35 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 222–269 | 48 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 231–249 | 16 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 231–237 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `14` (C): Annotated start 14 != Inferred start 26
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 3: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [11–25], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=26.
- ⚠️ Action 'Action_None' range [11-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-165] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [145-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-31] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-269] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-22] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-109] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-253] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-241] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>