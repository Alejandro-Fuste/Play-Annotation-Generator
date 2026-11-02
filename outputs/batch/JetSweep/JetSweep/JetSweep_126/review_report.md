# Play-Annotation-Generator Annotation Review — JetSweep_126

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_126`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 7 | START | 7 | 44 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 15 | START | 15 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `13` | `12` | 16 | START | 16 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 16 | START | 27 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 16 | START | 16 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `14` | 16 | START | 16 | 20 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 16 | START | 16 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 16 | START | 16 | 38 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 26 | END | 15 | 26 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 32 | START | 32 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 45 | START | 45 | 72 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `10` | `9` | 45 | START | 45 | 123 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 123 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 26 | 12 | inferred_complete_timeline |
| `Action_None` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_Toss` | 32 | 44 | 13 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 50 | 79 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LeadBlock` | 16 | 47 | 32 | inferred_complete_timeline |
| `Action_LeadBlock` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_LeadBlock` | 62 | 123 | 62 | inferred_complete_timeline |
| `Action_None` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 95 | 81 | inferred_complete_timeline |
| `Action_None` | 98 | 180 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 38 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 65 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 111 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 26 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 44 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 45 | 123 | 79 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 105 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 122 | 10 | inferred_complete_timeline |
| `Action_None` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 180 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 16 | 123 | 108 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 73 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 87 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 24 | 10 | inferred_complete_timeline |
| `Action_None` | 73 | 97 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 130 | 116 | inferred_complete_timeline |
| `Action_None` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 180 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 60 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 160 | 146 | inferred_complete_timeline |
| `Action_None` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 7–134 | 124 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 25–180 | 79 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 49–180 | 122 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 59–180 | 122 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 86–180 | 90 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 86–180 | 94 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 90–180 | 91 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 118–180 | 63 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 128–134 | 7 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 138–180 | 42 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 139–180 | 37 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 139–180 | 38 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 142–180 | 33 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 145–180 | 36 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 167–170 | 4 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 176–179 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

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
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 108 frames exceeds threshold 90 frames [start=16, end=123].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [15–26], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=27.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 96 frames exceeds threshold 90 frames [start=16, end=111].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '12' (RB) duration 108 frames exceeds threshold 90 frames [start=16, end=123].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 108 frames exceeds threshold 90 frames [start=16, end=123].
- ⚠️ Action 'Action_None' range [15-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-95] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-38] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [16-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [56-60] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [62-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [16-20] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [28-105] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [7-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [45-72] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>