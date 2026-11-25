# Play-Annotation-Generator Annotation Review — JetSweep_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_132`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE2 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 6 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 11 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `18` | `17` | 63 | START | 63 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 74 | START | 74 | 80 |
| ⚠️ START CHANGED | `Action_LeadBlock` | Position_Unknown | `21` | `20` | 75 | START | 88 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE2 | `8` | `7` | 75 | START | 75 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 75 | START | 75 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 75 | START | 75 | 134 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `13` | `12` | 75 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `14` | `13` | 75 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 75 | START | 75 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 87 | END | 74 | 87 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 91 | START | 91 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 103 | START | 103 | 106 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_Toss` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_None` | 104 | 145 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–150
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 28 | 23 | inferred_complete_timeline |
| `Action_None` | 80 | 136 | 57 | inferred_complete_timeline |
| `Action_None` | 138 | 150 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–160
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 73 | 63 | inferred_complete_timeline |
| `Action_None` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 83 | 160 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SealBlock` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_SealBlock` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_SealBlock` | 136 | 141 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 91 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 131 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 134 | 60 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 80 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 163 | 23 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 134 | 60 | inferred_complete_timeline |
| `Action_None` | 135 | 143 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 44 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 67 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 132 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 135 | 62 | inferred_complete_timeline |
| `Action_None` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_None` | 157 | 225 | 69 | inferred_complete_timeline |
| `Action_None` | 229 | 269 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 83 | 121 | 39 | inferred_complete_timeline |
| `Action_None` | 124 | 141 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 130 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 165 | 92 | inferred_complete_timeline |
| `Action_None` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 158 | 85 | inferred_complete_timeline |
| `Action_None` | 160 | 269 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 63–269 | 196 | 9 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 73–108 | 36 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 81–135 | 55 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 88–245 | 141 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 110–120 | 11 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 114–231 | 118 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 125–141 | 10 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 138–269 | 132 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 139–269 | 110 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 140–269 | 116 | 4 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 146–269 | 120 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 248–269 | 22 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `18` (3 segments found)
- ⚠️ `Action_LeadBlock` for actor_track_id `21` (Position_Unknown): Annotated start 75 != Inferred start 88
- ⚠️ Ambiguous match for action `Action_SealBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `13` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [74–87], lower_priority='Action_ZoneBlock' annotated_start=75, effective_Action_ZoneBlock_start=88.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=75, end=67. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-131] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-165] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [75-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [101-111] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [136-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [91-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [74-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-67] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-136] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [63-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [89-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-106] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [108-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [173-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-108] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [88-123] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-245] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-231] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '31' has 1 frames without a visible bounding box.
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