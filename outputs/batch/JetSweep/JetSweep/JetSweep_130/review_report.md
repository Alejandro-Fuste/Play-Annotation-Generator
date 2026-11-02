# Play-Annotation-Generator Annotation Review — JetSweep_130

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_130`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 17 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `17` | `16` | 8 | START | 18 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | DT1 | `14` | `13` | 16 | START | 16 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `5` | `4` | 18 | START | 18 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 18 | START | 18 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `12` | 18 | START | 18 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 18 | START | 18 | 115 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `7` | `6` | 18 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 18 | START | 18 | 44 |
| ✅ EXACT | `Action_SnapReceive` | C | `7` | `6` | 29 | END | 16 | 29 |
| ✅ EXACT | `Action_Toss` | C | `7` | `6` | 38 | START | 38 | 44 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `17` | `16` | 45 | START | 45 | 204 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `9` | `8` | 45 | START | 45 | 115 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LeadBlock` | 18 | 112 | 95 | inferred_complete_timeline |
| `Action_LeadBlock` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_None` | 116 | 137 | 22 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 67 | 52 | inferred_complete_timeline |
| `Action_None` | 69 | 98 | 30 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 115 | 98 | inferred_complete_timeline |
| `Action_None` | 116 | 189 | 74 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 115 | 98 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_None` | 30 | 37 | 8 | inferred_complete_timeline |
| `Action_Toss` | 38 | 44 | 7 | inferred_complete_timeline |
| `Action_None` | 45 | 111 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 105 | 88 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_None` | 116 | 132 | 17 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 44 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 45 | 115 | 71 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 167 | 45 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 15 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 21 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 36 | 41 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 176 | 161 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 192 | 177 | inferred_complete_timeline |
| `Action_None` | 196 | 209 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 17–210 | 177 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 18–204 | 187 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 24–76 | 53 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 37–186 | 106 | 6 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 70–210 | 141 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 88–176 | 81 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 100–138 | 39 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 118–210 | 93 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 119–210 | 92 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 122–146 | 25 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 161–210 | 50 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `17` (Position_Unknown): Annotated start 8 != Inferred start 18
- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 261: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '4' (RB) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=18, end=15. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 98 frames exceeds threshold 90 frames [start=18, end=115].
- ⚠️ Action 'Action_None' range [16-50] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-115] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [18-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-192] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [16-21] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [25-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-112] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [45-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-127] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '27' has 1 frames without a visible bounding box.
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

</details>