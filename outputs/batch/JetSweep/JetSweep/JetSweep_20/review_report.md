# Play-Annotation-Generator Annotation Review — JetSweep_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_20`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `19` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Toss` | QB | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR | offense | `19` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `3` | `2` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `4` | `3` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `8` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 57 | START | 57 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `1` | `0` | 61 | START | 61 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 61 | START | 61 | 90 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 61 | START | 71 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 61 | START | 61 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 61 | START | 61 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 61 | START | 61 | 112 |
| ✅ EXACT | `Action_JetMotion` | WR | `19` | `16` | 65 | START | 65 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 70 | END | 57 | 70 |
| ✅ EXACT | `Action_Toss` | QB | `2` | `1` | 80 | START | 80 | 90 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR | `19` | `16` | 91 | START | N/A | N/A |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `12` | `11` | 91 | START | 91 | 128 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `12` | `11` | 128 | BOUNDARY | 91 | 128 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `14` | `13` | 128 | BOUNDARY | N/A | 128 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `3` | `2` | 128 | BOUNDARY | 61 | 128 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `4` | `3` | 128 | BOUNDARY | N/A | 128 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `8` | `7` | 128 | BOUNDARY | N/A | 128 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_None` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_Toss` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_None` | 91 | 122 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_LeadBlock` | 61 | 106 | 46 | inferred_complete_timeline |
| `Action_LeadBlock` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 65–84
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 65 | 84 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 196 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 90 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 91 | 128 | 38 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 128 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 122 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 112 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 118 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 116 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 122 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 71 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 119 | 63 | inferred_complete_timeline |
| `Action_None` | 124 | 157 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 124 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 107 | 51 | inferred_complete_timeline |
| `Action_None` | 125 | 174 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 45–99
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_None` | 57 | 99 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–129 | 92 | 4 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 85–112 | 11 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 89–119 | 17 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 92–239 | 148 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 113–121 | 6 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 116–147 | 32 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 119–233 | 110 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 125–131 | 7 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 130–145 | 16 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 137–239 | 101 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 185–199 | 13 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 190–239 | 33 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 193–200 | 8 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 193–239 | 47 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 195–239 | 35 | 3 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 197–209 | 13 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 199–239 | 23 | 4 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 200–205 | 6 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 202–206 | 5 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 214–227 | 13 | 2 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 224–238 | 15 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 225–239 | 10 | 3 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 226–237 | 12 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 61 != Inferred start 71
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `19` (WR)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 42: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [57–70], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=71.
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=91, end=84. Clamping end to start.
- ⚠️ Action 'Action_LeadBlock' range [61-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-119] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-124] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-116] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-174] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [65-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-147] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-209] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-239] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-212] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-237] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.

</details>