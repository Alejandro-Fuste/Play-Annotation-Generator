# Play-Annotation-Generator Annotation Review — JetSweep_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_101`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 67
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
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 43
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | LT | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 78 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `17` | `16` | 77 | START | 78 | 105 |
| ✅ EXACT | `Action_BallSnap` | RG | `15` | `14` | 79 | START | 79 | 82 |
| ✅ EXACT | `Action_LeadBlock` | LT | `1` | `0` | 83 | START | 83 | 132 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `1` | `0` | 83 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 83 | START | 83 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 83 | START | 83 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 83 | START | 83 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 83 | START | 83 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `14` | `13` | 97 | END | 79 | 82 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 98 | START | 98 | 105 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `17` | `16` | 106 | START | 113 | 282 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 136 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_Toss` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_None` | 106 | 141 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 138 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 122 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_LeadBlock` | 83 | 132 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 131 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 136 | 45 | inferred_complete_timeline |
| `Action_None` | 137 | 137 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallSnap` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 136 | 54 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 136 | 54 | inferred_complete_timeline |
| `Action_None` | 137 | 144 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 129 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 169 | 91 | inferred_complete_timeline |
| `Action_None` | 174 | 233 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 88 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 115 | 37 | inferred_complete_timeline |
| `Action_None` | 118 | 259 | 142 | inferred_complete_timeline |
| `Action_None` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 254 | 176 | inferred_complete_timeline |
| `Action_None` | 260 | 277 | 18 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 94 | 16 | inferred_complete_timeline |
| `Action_None` | 98 | 117 | 20 | inferred_complete_timeline |
| `Action_None` | 119 | 171 | 53 | inferred_complete_timeline |
| `Action_None` | 173 | 214 | 42 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 139 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 78–282 | 198 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 121–141 | 21 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 121–136 | 16 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 127–131 | 4 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 131–195 | 60 | 3 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 144–299 | 156 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 146–177 | 32 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 150–299 | 150 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 197–299 | 103 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 205–227 | 21 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 248–299 | 51 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `17` (Position_Unknown): Annotated start 77 != Inferred start 78
- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (LT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `14` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `17` (Position_Unknown): Annotated start 106 != Inferred start 113

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 83 for track '0': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
- ⚠️ Action 'Action_LeadBlock' range [83-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-115] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-259] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-122] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-169] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-233] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-90] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 137, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [137-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [79-82] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [78-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-282] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-171] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-195] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '26' has 1 frames without a visible bounding box.
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

</details>