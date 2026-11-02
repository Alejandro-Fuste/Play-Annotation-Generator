# Play-Annotation-Generator Annotation Review — JetSweep_166

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_166`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_LeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `17` | `16` | 90 | START | 92 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 92 | START | 92 | 106 |
| ✅ EXACT | `Action_LeadBlock` | LT | `3` | `2` | 93 | START | 93 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 93 | START | 93 | 106 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `3` | `2` | 93 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 93 | START | 93 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 93 | START | 93 | 121 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `9` | `8` | 93 | START | 107 | 126 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 106 | END | 92 | 106 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 113 | START | 113 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `17` | `16` | 121 | START | 121 | 123 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 126 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 92 | 106 | 15 | inferred_complete_timeline |
| `Action_None` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_Toss` | 113 | 120 | 8 | inferred_complete_timeline |
| `Action_None` | 121 | 165 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 109 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 228 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_LeadBlock` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_None` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_None` | 141 | 162 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 121 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 127 | 173 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_BallSnap` | 92 | 106 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 126 | 20 | inferred_complete_timeline |
| `Action_None` | 127 | 140 | 14 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 20 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 106 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 152 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 222 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 123 | 32 | inferred_complete_timeline |
| `Action_None` | 125 | 149 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 27–101
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 91 | 65 | inferred_complete_timeline |
| `Action_None` | 92 | 101 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 127 | 19 | inferred_complete_timeline |
| `Action_None` | 144 | 168 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 209 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_None` | 92 | 155 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–160 | 161 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 92–299 | 189 | 9 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 93–191 | 94 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 102–155 | 54 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 115–132 | 18 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 150–162 | 13 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 154–155 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 156–243 | 86 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 164–299 | 136 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 174–299 | 89 | 4 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 189–299 | 111 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 204–299 | 87 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 208–299 | 92 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 235–250 | 16 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 256–299 | 44 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 269–279 | 11 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 272–276 | 5 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 279–299 | 21 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 280–281 | 2 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 283–299 | 17 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `3` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `9` (C): Annotated start 93 != Inferred start 107
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 93 for track '2': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [92–106], lower_priority='Action_ZoneBlock' annotated_start=93, effective_Action_ZoneBlock_start=107.
- ⚠️ Action 'Action_None' range [92-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-162] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-222] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-165] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-20] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-106] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [92-115] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-293] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-161] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-155] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-279] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>