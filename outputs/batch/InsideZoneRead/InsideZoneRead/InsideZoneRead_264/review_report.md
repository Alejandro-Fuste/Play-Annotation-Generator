# Play-Annotation-Generator Annotation Review — InsideZoneRead_264

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_264`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 8 | START | 8 | 20 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 11 | START | 21 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 11 | START | 11 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 11 | START | 11 | 44 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 20 | END | 8 | 20 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 23 | START | 23 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `14` | `13` | 28 | START | 28 | 30 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 32 | START | 32 | 35 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `12` | `11` | 44 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 79 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_None` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_Keep` | 32 | 35 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_None` | 49 | 98 | 50 | inferred_complete_timeline |
| `Action_None` | 107 | 211 | 105 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 55 | 48 | inferred_complete_timeline |
| `Action_None` | 58 | 116 | 59 | inferred_complete_timeline |
| `Action_None` | 118 | 158 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 79 | 53 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 96 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 32 | 57 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 63 | 70 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 79 | 25 | inferred_complete_timeline |
| `Action_None` | 80 | 96 | 17 | inferred_complete_timeline |
| `Action_None` | 101 | 121 | 21 | inferred_complete_timeline |
| `Action_None` | 139 | 169 | 31 | inferred_complete_timeline |
| `Action_None` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 76 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 183 | 176 | inferred_complete_timeline |
| `Action_None` | 187 | 229 | 43 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 17 | 10 | inferred_complete_timeline |
| `Action_None` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_None` | 34 | 156 | 123 | inferred_complete_timeline |
| `Action_None` | 159 | 181 | 23 | inferred_complete_timeline |
| `Action_None` | 184 | 201 | 18 | inferred_complete_timeline |
| `Action_None` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_None` | 48 | 62 | 15 | inferred_complete_timeline |
| `Action_None` | 65 | 92 | 28 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 27 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_None` | 36 | 87 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 95 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–238 | 220 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 11–146 | 136 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 31–32 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 59–129 | 71 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 76–186 | 70 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 82–159 | 78 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 83–138 | 55 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 91–222 | 85 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 97–236 | 132 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 105–118 | 14 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 108–131 | 24 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 141–239 | 96 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 162–239 | 76 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 181–184 | 4 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 182–231 | 50 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 184–239 | 56 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 189–192 | 4 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 11 != Inferred start 21
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `14` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `12` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 528: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '11' has invalid range: start=44, end=35. Clamping end to start.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [8–20], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=21.
- ⚠️ Action 'Action_None' range [8-27] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-50] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-23] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-55] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-40] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-211] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-44] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-121] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-17] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-25] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-181] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-27] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [28-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [32-57] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [63-70] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-222] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-172] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-131] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-180] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-231] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>