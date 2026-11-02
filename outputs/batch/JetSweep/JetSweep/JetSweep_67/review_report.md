# Play-Annotation-Generator Annotation Review — JetSweep_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_67`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `23` | `20` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 76 | START | 76 | 88 |
| ✅ EXACT | `Action_LeadBlock` | TE | `8` | `7` | 77 | START | 77 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `0` | 77 | START | 77 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 77 | START | 77 | 80 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 77 | START | 89 | 126 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 77 | START | 77 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 77 | START | 77 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 88 | END | 76 | 88 |
| ❌ MISSING SEGMENT | `Action_JetMotion` | Position_Unknown | `23` | `20` | 89 | START | N/A | N/A |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 100 | START | 100 | 105 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `1` | `0` | 103 | START | 103 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `20` | 106 | START | 117 | 164 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 135 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 88 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 99 | 11 | inferred_complete_timeline |
| `Action_Toss` | 100 | 105 | 6 | inferred_complete_timeline |
| `Action_None` | 106 | 130 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 125 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 87–115
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 87 | 115 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_LeadBlock` | 77 | 108 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 134 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 102 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 103 | 127 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 88 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 126 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 98 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 121 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 114 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 97 | 22 | inferred_complete_timeline |
| `Action_None` | 100 | 118 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 59 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 142 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 89 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 129 | 54 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 127 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 104 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–3
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 9–73 | 58 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 92–269 | 177 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 117–269 | 144 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 124–126 | 3 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 127–269 | 115 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 130–212 | 82 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 183–259 | 74 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 188–269 | 82 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 205–245 | 38 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 233–269 | 32 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 242–269 | 25 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 253–269 | 15 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 77 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ❌ Missing segment for action `Action_JetMotion` on target `23` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (3 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [76–88], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=89.
- ⚠️ Segment 'Action_JetMotion' for track '20' has invalid range: start=117, end=105. Clamping end to start.
- ⚠️ Action 'Action_BlockSecondLevel' range [103-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-118] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [77-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [89-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-73] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-115] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-115] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-164] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-209] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-259] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-240] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-259] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>