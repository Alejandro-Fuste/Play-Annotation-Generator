# Play-Annotation-Generator Annotation Review — JetSweep_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_164`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 11 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 11 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 11 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 11 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 11 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 11 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 11 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 11 | 68 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `15` | `14` | 32 | START | 32 | 91 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 68 | START | 68 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `4` | `3` | 69 | START | 69 | 137 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 69 | START | 69 | 128 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 69 | START | 81 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `16` | 69 | START | 69 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 69 | START | 69 | 116 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 80 | END | 68 | 80 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 88 | START | 88 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `15` | `14` | 92 | START | 92 | 94 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 218 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–134
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_None` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_Toss` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 92 | 1 | inferred_complete_timeline |
| `Action_None` | 96 | 134 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 11–78
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 78 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 11–82
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 82 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 11–263
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 68 | 58 | inferred_complete_timeline |
| `Action_LeadBlock` | 69 | 137 | 69 | inferred_complete_timeline |
| `Action_LeadBlock` | 141 | 218 | 78 | inferred_complete_timeline |
| `Action_None` | 219 | 263 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 11–128
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 68 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 128 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–130
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 36 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 68 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 130 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 11–133
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 68 | 80 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 133 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–170
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 68 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 116 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 170 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–125
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 79 | 125 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 232 | 165 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 11–152
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 105 | 38 | inferred_complete_timeline |
| `Action_None` | 110 | 152 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–128
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 101 | 34 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 128 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 245 | 178 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 11–217
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 198 | 131 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–295
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 265 | 198 | inferred_complete_timeline |
| `Action_None` | 272 | 295 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–80
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 67 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 11–166 | 148 | 5 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 81–178 | 95 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 91–119 | 29 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 112–144 | 28 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 118–147 | 29 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 120–132 | 13 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 138–299 | 149 | 4 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 193–296 | 102 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 197–250 | 50 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 205–299 | 92 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 211–248 | 25 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 216–288 | 73 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 219–299 | 81 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 239–261 | 23 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 249–299 | 51 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 271–292 | 22 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 275–299 | 8 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 278–289 | 12 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 69 != Inferred start 81
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 330: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '3' (TE) duration 150 frames exceeds threshold 90 frames [start=69, end=218].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 102 frames exceeds threshold 90 frames [start=69, end=170].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [68–80], lower_priority='Action_ZoneBlock' annotated_start=69, effective_Action_ZoneBlock_start=81.
- ⚠️ Action 'Action_ZoneBlock' range [69-128] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-245] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [69-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [141-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-263] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-265] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-295] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-116] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 92, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [92-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-133] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-68] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-130] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-141] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-142] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-247] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-296] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-230] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-228] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-292] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-289] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>