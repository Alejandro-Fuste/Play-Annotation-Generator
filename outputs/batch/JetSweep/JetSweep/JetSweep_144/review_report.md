# Play-Annotation-Generator Annotation Review — JetSweep_144

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_144`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Toss` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 70 | START | 70 | 84 |
| ✅ EXACT | `Action_LeadBlock` | RB | `3` | `2` | 72 | START | 72 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 72 | START | 72 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 72 | START | 72 | 134 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 72 | START | 85 | 130 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 72 | START | 72 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 72 | START | 72 | 120 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `17` | `16` | 77 | START | 77 | 102 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 84 | END | 70 | 84 |
| ✅ EXACT | `Action_Toss` | QB | `2` | `1` | 87 | START | 87 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 103 | START | 104 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 137 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_None` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_Toss` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_None` | 103 | 135 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_LeadBlock` | 72 | 137 | 66 | inferred_complete_timeline |
| `Action_None` | 138 | 156 | 19 | inferred_complete_timeline |
| `Action_None` | 158 | 166 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 174 | 105 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 209 | 29 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 134 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 137 | 66 | inferred_complete_timeline |
| `Action_None` | 138 | 152 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 130 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 91 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 124 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 120 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 137 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 239 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 122 | 53 | inferred_complete_timeline |
| `Action_None` | 125 | 132 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 140 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 69 | 59 | inferred_complete_timeline |
| `Action_None` | 70 | 88 | 19 | inferred_complete_timeline |
| `Action_None` | 92 | 130 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 131 | 62 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 177 | 14 | inferred_complete_timeline |
| `Action_None` | 180 | 217 | 38 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 138 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 65–67 | 3 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 75–78 | 4 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 77–239 | 161 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 102–107 | 6 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 109–128 | 19 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 112–161 | 49 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 132–136 | 5 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 139–239 | 90 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 161–239 | 79 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 164–236 | 73 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 183–239 | 51 | 5 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 185–239 | 53 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 219–239 | 21 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 72 != Inferred start 85
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [70–84], lower_priority='Action_ZoneBlock' annotated_start=72, effective_Action_ZoneBlock_start=85.
- ⚠️ Action 'Action_ZoneBlock' range [72-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-124] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-135] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [72-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-209] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-131] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-217] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-140] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [77-102] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-161] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-217] for track '26' has 1 frames without a visible bounding box.
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