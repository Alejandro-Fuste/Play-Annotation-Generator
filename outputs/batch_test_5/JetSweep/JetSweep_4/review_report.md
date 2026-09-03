# TapeVision Annotation Review — JetSweep_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_4`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `29` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `19` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | TE | offense | `4` | `3` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `9` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `29` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 95 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `19` | `17` | 73 | START | 115 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `15` | `14` | 90 | START | 90 | 106 |
| ✅ EXACT | `Action_LeadBlock` | TE | `4` | `3` | 95 | START | 95 | 154 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 96 | START | 96 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `17` | 96 | START | 116 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 96 | START | 96 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 96 | START | 96 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 96 | START | 96 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 110 | END | 73 | 110 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 116 | START | 116 | 125 |
| ✅ EXACT | `Action_BallCarry` | WR | `15` | `14` | 126 | START | 126 | 145 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `11` | `10` | 154 | BOUNDARY | 96 | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `19` | `17` | 154 | BOUNDARY | N/A | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `2` | `1` | 154 | BOUNDARY | N/A | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | TE | `4` | `3` | 154 | BOUNDARY | 95 | 154 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `9` | `8` | 154 | BOUNDARY | N/A | 154 |

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
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 110 | 38 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_Toss` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_None` | 126 | 149 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 242 | 170 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 90–145
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_JetMotion` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 145 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `29`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `29`
- **team_side:** `offense`
- **Visible Frames:** 179–357
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 179 | 274 | 96 | inferred_complete_timeline |
| `Action_None` | 279 | 357 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_LeadBlock` | 95 | 154 | 60 | inferred_complete_timeline |
| `Action_None` | 155 | 155 | 1 | inferred_complete_timeline |
| `Action_None` | 158 | 359 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 111 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 146 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 115–149
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 149 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 121 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 154 | 59 | inferred_complete_timeline |
| `Action_None` | 155 | 155 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 143 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 105–359
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 119 | 141 | 23 | inferred_complete_timeline |
| `Action_None` | 144 | 174 | 31 | inferred_complete_timeline |
| `Action_None` | 177 | 359 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `23`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 139–158
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 139 | 158 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT-1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 118 | 46 | inferred_complete_timeline |
| `Action_None` | 121 | 134 | 14 | inferred_complete_timeline |
| `Action_None` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 148 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 120 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 136 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 130 | 42 | inferred_complete_timeline |
| `Action_None` | 139 | 207 | 69 | inferred_complete_timeline |
| `Action_None` | 210 | 329 | 120 | inferred_complete_timeline |
| `Action_None` | 332 | 359 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–36 | 15 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 113–280 | 161 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 138–141 | 4 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 146–185 | 40 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 171–328 | 83 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 205–274 | 70 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 224–359 | 136 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 239–241 | 3 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 249–359 | 111 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 268–333 | 63 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 269–359 | 77 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 278–309 | 19 | 4 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 294–305 | 9 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 302–317 | 16 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 302–359 | 58 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 303–354 | 52 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 320–359 | 40 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 347–359 | 13 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `19` (C): Annotated start 73 != Inferred start 115
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=115, end=110. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [115–115], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=116.
- ⚠️ Action 'Action_None' range [73-120] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-146] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 155, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [155-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-154] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 155, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [155-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-85] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-329] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [90-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-359] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-280] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-149] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-158] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-274] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-357] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-274] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-333] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-277] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-354] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-305] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-317] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>