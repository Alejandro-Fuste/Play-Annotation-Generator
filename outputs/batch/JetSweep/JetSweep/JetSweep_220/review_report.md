# Play-Annotation-Generator Annotation Review — JetSweep_220

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_220`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 96 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `3` | `2` | 74 | START | 74 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 94 | START | 94 | 105 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `4` | `3` | 97 | START | 97 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 97 | START | 97 | 118 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `11` | 97 | START | 106 | 119 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 97 | START | 97 | 150 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 97 | START | 97 | 111 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 105 | END | 94 | 105 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 116 | START | 116 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `3` | `2` | 122 | START | 129 | 148 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_SnapReceive` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_None` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_Toss` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 165 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 93 | 46 | inferred_complete_timeline |
| `Action_None` | 94 | 112 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_LeadBlock` | 97 | 127 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 131 | 38 | inferred_complete_timeline |
| `Action_None` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 111 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_BallSnap` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 119 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 118 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 150 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 132 | 39 | inferred_complete_timeline |
| `Action_None` | 134 | 176 | 43 | inferred_complete_timeline |
| `Action_None` | 178 | 213 | 36 | inferred_complete_timeline |
| `Action_None` | 216 | 276 | 61 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 136 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 176 | 83 | inferred_complete_timeline |
| `Action_None` | 181 | 220 | 40 | inferred_complete_timeline |
| `Action_None` | 225 | 266 | 42 | inferred_complete_timeline |
| `Action_None` | 271 | 299 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 158 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 160 | 67 | inferred_complete_timeline |
| `Action_None` | 162 | 209 | 48 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 250 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 163 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–160 | 130 | 4 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–161 | 162 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–166 | 156 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 99–147 | 49 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 104–179 | 13 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 109–153 | 45 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 122–161 | 38 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 124–199 | 64 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 138–150 | 13 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 151–158 | 8 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 154–155 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 156–171 | 16 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 164–273 | 67 | 6 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 165–234 | 63 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 166–216 | 35 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 171–259 | 82 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 174–270 | 97 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 180–224 | 45 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 226–261 | 36 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 231–299 | 60 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 239–290 | 51 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 245–293 | 49 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 250–299 | 50 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 279–299 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 97 != Inferred start 106
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 442: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [94–105], lower_priority='Action_ZoneBlock' annotated_start=97, effective_Action_ZoneBlock_start=106.
- ⚠️ Action 'Action_None' range [94-158] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [74-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-160] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [97-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-276] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-209] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-250] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-145] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-261] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-282] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-271] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>