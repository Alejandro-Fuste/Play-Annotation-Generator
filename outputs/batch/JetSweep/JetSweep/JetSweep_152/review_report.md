# Play-Annotation-Generator Annotation Review — JetSweep_152

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_152`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `17` | 70 | START | 70 | 85 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 76 | START | 76 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 78 | START | 78 | 86 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 78 | START | 90 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `1` | 78 | START | 78 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `2` | 78 | START | 78 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 78 | START | 78 | 123 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 89 | END | 76 | 89 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 93 | START | 93 | 97 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `19` | `17` | 98 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 123 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_None` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_Toss` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 133 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 121 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 236 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 105 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 86 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 123 | 46 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 121 | 32 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 123 | 46 | inferred_complete_timeline |
| `Action_None` | 124 | 132 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 123 | 46 | inferred_complete_timeline |
| `Action_None` | 124 | 241 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 122 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 96 | 21 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 129 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 220 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 112 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 125 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 269 | 194 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 70–85 | 16 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 84–116 | 33 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 84–224 | 141 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 87–129 | 13 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 114–125 | 10 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 125–131 | 7 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 135–269 | 135 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 141–269 | 115 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 147–269 | 118 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 157–210 | 54 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 160–165 | 6 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 169–243 | 75 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 215–258 | 42 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 234–269 | 29 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 244–269 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 78 != Inferred start 90
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [76–89], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=90.
- ⚠️ Segment 'Action_BallCarry' for track '17' has invalid range: start=98, end=85. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [78-86] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-236] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [70-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-224] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-243] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-269] for track '31' has 2 frames without a visible bounding box.
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

</details>