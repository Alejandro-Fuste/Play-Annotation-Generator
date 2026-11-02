# Play-Annotation-Generator Annotation Review — JetSweep_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_91`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DE1 | defense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 32 | START | 32 | 43 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `6` | `5` | 35 | START | 35 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 35 | START | 44 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 35 | START | 35 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 35 | START | 35 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 35 | START | 35 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 35 | START | 35 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DE1 | `17` | `16` | 36 | START | 36 | 36 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 43 | END | 32 | 43 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 47 | START | 47 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 60 | START | 60 | 61 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_SnapReceive` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_Toss` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 101 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 92 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 50 | 19 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 168 | 74 | inferred_complete_timeline |
| `Action_None` | 174 | 181 | 8 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_LeadBlock` | 35 | 65 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 66 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 91 | 21 | inferred_complete_timeline |
| `Action_None` | 92 | 119 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 60 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 91 | 30 | inferred_complete_timeline |
| `Action_None` | 92 | 100 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 70 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 91 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 88 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_JetMotion` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 45 | 81 | 37 | inferred_complete_timeline |
| `Action_JetMotion` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 42 | 11 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 92 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 37 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 105 | 74 | inferred_complete_timeline |
| `Action_None` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_None` | 130 | 152 | 23 | inferred_complete_timeline |
| `Action_None` | 154 | 269 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 223 | 192 | inferred_complete_timeline |
| `Action_None` | 227 | 269 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_None` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_None` | 55 | 66 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 196 | 165 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 19–83 | 60 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 36–269 | 214 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 85–88 | 4 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 95–103 | 9 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 99–128 | 30 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 104–269 | 151 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 136–140 | 5 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 173–228 | 39 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 180–269 | 80 | 4 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 200–207 | 8 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 207–212 | 6 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 229–269 | 41 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 232–247 | 16 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 239–269 | 31 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 264–269 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [32–43], lower_priority='Action_ZoneBlock' annotated_start=35, effective_Action_ZoneBlock_start=44.
- ⚠️ Action 'Action_None' range [32-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-88] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-44] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-66] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-42] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-196] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [35-65] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-91] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-105] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-128] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-152] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-92] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-17] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' for track '16' starts at frame 36, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_JetMotion' range [36-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [45-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '34' has 1 frames without a visible bounding box.
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

</details>