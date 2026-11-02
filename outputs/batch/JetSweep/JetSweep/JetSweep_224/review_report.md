# Play-Annotation-Generator Annotation Review — JetSweep_224

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_224`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `18` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `10` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 67 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `20` | `18` | 64 | START | 65 | 89 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `15` | `14` | 66 | START | 66 | 75 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `3` | `2` | 68 | START | 68 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 68 | START | 68 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `1` | 68 | START | 68 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 68 | START | 68 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 68 | START | 68 | 103 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 75 | END | 66 | 75 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 83 | START | 83 | 89 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `20` | `18` | 90 | START | 90 | 215 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_SnapReceive` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_Toss` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_None` | 90 | 173 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 216 | 151 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_LeadBlock` | 68 | 98 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 103 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 127 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 133 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 145 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 147 | 1 | inferred_complete_timeline |
| `Action_None` | 148 | 159 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 147 | 80 | inferred_complete_timeline |
| `Action_None` | 148 | 159 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 111 | 46 | inferred_complete_timeline |
| `Action_None` | 113 | 162 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_BallSnap` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_None` | 78 | 137 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 71 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 92 | 27 | inferred_complete_timeline |
| `Action_None` | 98 | 167 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–151
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 65 | 63 | inferred_complete_timeline |
| `Action_None` | 66 | 151 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 60–239 | 128 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 65–215 | 151 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 92–186 | 90 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 100–239 | 140 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 130–131 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 136–151 | 16 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 143–145 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 144–239 | 94 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 144–214 | 60 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 146–217 | 72 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 146–179 | 6 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 150–239 | 90 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 150–152 | 3 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 168–197 | 12 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 187–193 | 7 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 192–239 | 48 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 235–239 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `20` (Position_Unknown): Annotated start 64 != Inferred start 65
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 450: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [66-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-145] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [68-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-216] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [66-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-111] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-117] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-215] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-193] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '39' has 1 frames without a visible bounding box.
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