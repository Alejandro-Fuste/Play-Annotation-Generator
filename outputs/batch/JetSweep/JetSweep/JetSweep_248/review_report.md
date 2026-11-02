# Play-Annotation-Generator Annotation Review — JetSweep_248

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_248`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | RT | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Toss` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 84 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 76 | START | 76 | 112 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 86 | START | 86 | 98 |
| ✅ EXACT | `Action_LeadBlock` | RT | `1` | `0` | 87 | START | 87 | 158 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `1` | `0` | 87 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 87 | START | 99 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `16` | 87 | START | 87 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 87 | START | 87 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 87 | START | 87 | 162 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 98 | END | 86 | 98 |
| ✅ EXACT | `Action_Toss` | QB | `3` | `2` | 109 | START | 109 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 113 | START | 113 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 162 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_Toss` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 146 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 238 | 153 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 102 | 17 | inferred_complete_timeline |
| `Action_None` | 104 | 194 | 91 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 84–132
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 132 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 162 | 76 | inferred_complete_timeline |
| `Action_None` | 163 | 196 | 34 | inferred_complete_timeline |
| `Action_None` | 199 | 299 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 162 | 64 | inferred_complete_timeline |
| `Action_None` | 163 | 183 | 21 | inferred_complete_timeline |
| `Action_None` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 162 | 76 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_LeadBlock` | 87 | 158 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 117 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 103 | 18 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 171 | 20 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 97 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 184 | 99 | inferred_complete_timeline |
| `Action_None` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_None` | 194 | 227 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 141 | 56 | inferred_complete_timeline |
| `Action_None` | 144 | 148 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 147 | 62 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 96 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 235 | 138 | inferred_complete_timeline |
| `Action_None` | 237 | 242 | 6 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 12–299 | 193 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 76–242 | 158 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 91–120 | 29 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 124–299 | 86 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 126–299 | 161 | 6 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 132–299 | 137 | 9 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 133–166 | 12 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 143–196 | 51 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 160–164 | 5 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 164–182 | 15 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 167–175 | 9 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 170–299 | 130 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 174–298 | 123 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 175–230 | 56 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 177–299 | 98 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 199–299 | 99 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 202–234 | 32 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 218–299 | 82 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 234–299 | 56 | 5 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 245–299 | 55 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 251–254 | 4 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 255–281 | 14 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (RT)
- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 87 != Inferred start 99
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 87 for track '0': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [86–98], lower_priority='Action_ZoneBlock' annotated_start=87, effective_Action_ZoneBlock_start=99.
- ⚠️ Action 'Action_LeadBlock' range [87-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-238] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-141] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-235] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-171] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-227] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-117] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-232] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [240-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-280] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-252] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-298] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-230] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-251] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-234] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-249] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-273] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>