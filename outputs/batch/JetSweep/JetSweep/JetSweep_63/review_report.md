# Play-Annotation-Generator Annotation Review — JetSweep_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_63`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `15` | 63 | START | 63 | 96 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 67 | START | 67 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `11` | `10` | 73 | START | 73 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 73 | START | 73 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `1` | 73 | START | 73 | 141 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `3` | `2` | 73 | START | 80 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `4` | 73 | START | 73 | 141 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 73 | START | 73 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 79 | END | 67 | 79 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 87 | START | 87 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `16` | `15` | 97 | START | 97 | 133 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `6` | `5` | 105 | START | 105 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 141 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SnapReceive` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_Toss` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 125 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_LeadBlock` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_LeadBlock` | 82 | 141 | 60 | inferred_complete_timeline |
| `Action_None` | 142 | 168 | 27 | inferred_complete_timeline |
| `Action_None` | 170 | 208 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 269 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_None` | 142 | 142 | 1 | inferred_complete_timeline |
| `Action_None` | 145 | 165 | 21 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_BallSnap` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 141 | 62 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 104 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 105 | 141 | 37 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 83 | 17 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 269 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 110 | 44 | inferred_complete_timeline |
| `Action_None` | 112 | 269 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 103 | 37 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 269 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 187 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 123 | 57 | inferred_complete_timeline |
| `Action_None` | 131 | 267 | 137 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 62–208 | 145 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 88–123 | 36 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 119–269 | 148 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 130–176 | 13 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 137–252 | 116 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 146–153 | 6 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 146–269 | 85 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 160–165 | 6 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 169–269 | 101 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 174–179 | 6 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 177–179 | 3 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 177–183 | 7 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 181–269 | 89 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 187–269 | 83 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 187–258 | 72 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 211–228 | 12 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 215–269 | 50 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 243–269 | 26 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 256–268 | 9 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 257–268 | 9 | 3 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 259–266 | 8 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `3` (C): Annotated start 73 != Inferred start 80
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [67–79], lower_priority='Action_ZoneBlock' annotated_start=73, effective_Action_ZoneBlock_start=80.
- ⚠️ Action 'Action_None' range [67-187] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [73-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-110] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 142, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [142-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '15' starts at frame 97, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [97-133] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-208] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-258] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-232] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-254] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>