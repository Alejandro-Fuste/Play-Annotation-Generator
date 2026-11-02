# Play-Annotation-Generator Annotation Review — JetSweep_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_35`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | WR | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `3` | `2` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `5` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | `10` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 76 | START | 76 | 87 |
| ✅ EXACT | `Action_JetMotion` | WR | `17` | `16` | 78 | START | 78 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 79 | START | 79 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 79 | START | 100 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 79 | START | 79 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 79 | START | 79 | 132 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 92 | END | 76 | 92 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 98 | START | 98 | 106 |
| ✅ EXACT | `Action_BallCarry` | WR | `17` | `16` | 107 | START | 107 | 299 |
| ✅ EXACT | `Action_LeadBlock` | WR | `2` | `1` | 107 | START | 107 | 132 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `12` | `11` | 132 | BOUNDARY | 118 | 132 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `14` | `13` | 132 | BOUNDARY | 118 | 132 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `3` | `2` | 132 | BOUNDARY | N/A | 132 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `5` | `4` | 132 | BOUNDARY | 79 | 132 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 92 | 17 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_Toss` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_None` | 107 | 135 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_LeadBlock` | 107 | 132 | 26 | inferred_complete_timeline |
| `Action_None` | 133 | 224 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 78–299
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 78 | 106 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 299 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>TE-Y — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 121 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 128 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 132 | 54 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 114 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_None` | 133 | 133 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 100 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 132 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 126 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 129 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 125 | 50 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 117 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 170 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 122 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_None` | 76 | 162 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 75 | 60 | inferred_complete_timeline |
| `Action_None` | 76 | 87 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–164 | 165 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 84–89 | 5 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 86–131 | 46 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 100–299 | 172 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 124–131 | 8 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 135–299 | 165 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 170–288 | 116 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 175–299 | 125 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 218–299 | 29 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 222–224 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 227–267 | 41 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 234–299 | 59 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 251–299 | 16 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 272–299 | 28 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 275–299 | 25 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 285–299 | 14 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 72: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [76–92], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=93.
- ⚠️ Action 'Action_None' range [76-170] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-164] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-135] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-132] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [76-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-132] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 133, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [133-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-131] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-265] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>