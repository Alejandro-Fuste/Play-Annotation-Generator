# Play-Annotation-Generator Annotation Review — JetSweep_196

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_196`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `14` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `14` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 2 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 9 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `18` | `14` | 81 | START | 82 | 94 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 88 | START | 88 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | Position_Unknown | `14` | `12` | 89 | START | 89 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 89 | START | 100 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 89 | START | 93 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `11` | 89 | START | 89 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `15` | 89 | START | 89 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 89 | START | 89 | 114 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 99 | END | 88 | 99 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 104 | START | 104 | 108 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `18` | `14` | 109 | START | 109 | 176 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 117 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–193
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_Toss` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_None` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 126 | 193 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 114 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 117 | 1 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–197
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 69 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 117 | 25 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 128 | 197 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 87 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 117 | 18 | inferred_complete_timeline |
| `Action_None` | 118 | 148 | 31 | inferred_complete_timeline |
| `Action_None` | 150 | 188 | 39 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 256 | 56 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–173
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 88 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 117 | 29 | inferred_complete_timeline |
| `Action_None` | 118 | 137 | 20 | inferred_complete_timeline |
| `Action_None` | 140 | 173 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 89–90
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 89 | 90 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 121 | 34 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 106 | 19 | inferred_complete_timeline |
| `Action_None` | 108 | 132 | 25 | inferred_complete_timeline |
| `Action_None` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 190 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 119 | 32 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 222 | 75 | inferred_complete_timeline |
| `Action_None` | 224 | 251 | 28 | inferred_complete_timeline |
| `Action_None` | 258 | 264 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_None` | 88 | 114 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–269 | 257 | 5 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–101 | 89 | 4 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 11–114 | 102 | 3 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 80–233 | 153 | 3 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 82–176 | 94 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 104–186 | 52 | 3 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 105–107 | 3 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 109–111 | 3 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 123–269 | 100 | 7 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 130–176 | 41 | 3 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 131–160 | 30 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 133–143 | 11 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 136–256 | 106 | 4 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 153–264 | 102 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 159–269 | 107 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 175–180 | 6 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 214–269 | 53 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 243–269 | 20 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 393: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [88–99], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=100.
- ⚠️ Action 'Action_None' range [88-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-222] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-251] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [88-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-256] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-197] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [89-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [94-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-233] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [82-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [109-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-118] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-160] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-154] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-249] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-256] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>