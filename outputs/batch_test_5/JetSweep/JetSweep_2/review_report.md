# TapeVision Annotation Review — JetSweep_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_2`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 9 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `6` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 96 |
| ✅ EXACT | `Action_JetMotion` | WR | `5` | `4` | 48 | START | 48 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 96 | START | 96 | 108 |
| ✅ EXACT | `Action_LeadBlock` | TE | `15` | `14` | 97 | START | 97 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 97 | START | 97 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 97 | START | 109 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 97 | START | 97 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 97 | START | 107 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 97 | START | 97 | 132 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 108 | END | 96 | 108 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 116 | START | 116 | 121 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `17` | `16` | 122 | START | 124 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–221
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_Toss` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 170 | 49 | inferred_complete_timeline |
| `Action_None` | 173 | 221 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_JetMotion` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_None` | 49 | 70 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 176 | 81 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 96 | 88 | inferred_complete_timeline |
| `Action_LeadBlock` | 97 | 148 | 52 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 148 | 52 | inferred_complete_timeline |
| `Action_None` | 149 | 161 | 13 | inferred_complete_timeline |
| `Action_None` | 180 | 208 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 107–162
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 149 | 162 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 9 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 95 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 114 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_None` | 149 | 218 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 132 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_None` | 149 | 173 | 25 | inferred_complete_timeline |
| `Action_None` | 177 | 206 | 30 | inferred_complete_timeline |
| `Action_None` | 208 | 222 | 15 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 96 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 148 | 52 | inferred_complete_timeline |
| `Action_None` | 149 | 169 | 21 | inferred_complete_timeline |
| `Action_None` | 174 | 229 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 184 | 89 | inferred_complete_timeline |
| `Action_None` | 189 | 205 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 16–170
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 95 | 46 | inferred_complete_timeline |
| `Action_None` | 96 | 170 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 176 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 30 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 196 | 101 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 177 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 206 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 158 | 63 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 74–158 | 82 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 90–128 | 39 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 98–206 | 108 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 105–125 | 19 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 132–201 | 50 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 145–208 | 62 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 199–206 | 8 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 209–291 | 83 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 212–228 | 15 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 216–299 | 76 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 216–232 | 17 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 219–299 | 75 | 4 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 221–298 | 78 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 223–299 | 75 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 230–294 | 65 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 231–299 | 64 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 234–299 | 66 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `17` (Position_Unknown): Annotated start 122 != Inferred start 124

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 4 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 6: Duplicate assignment for track ID '?' in grid. Overwriting previous assignment.
- ⚠️ Invalid track ID '?' in Player Track ID sheet. Must be an integer.
- ⚠️ Segment 'Action_JetMotion' for track '4' has invalid range: start=48, end=0. Clamping end to start.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [96–108], lower_priority='Action_ZoneBlock' annotated_start=97, effective_Action_ZoneBlock_start=109.
- ⚠️ Action 'Action_None' range [96-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-184] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-132] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [116-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-114] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-48] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-120] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-158] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-206] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-140] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-171] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-208] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-291] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-298] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-255] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-261] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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