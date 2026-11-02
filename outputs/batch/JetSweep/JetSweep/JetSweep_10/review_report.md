# Play-Annotation-Generator Annotation Review — JetSweep_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_10`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `15` | `14` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `5` | `4` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `7` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `15` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 98 |
| ✅ EXACT | `Action_JetMotion` | WR | `15` | `14` | 88 | START | 88 | 112 |
| ✅ EXACT | `Action_LeadBlock` | RB | `4` | `3` | 91 | START | 91 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 91 | START | 91 | 161 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `13` | `12` | 91 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 91 | START | 91 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `4` | 91 | START | 91 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 91 | START | 91 | 144 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 99 | START | 99 | 102 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 102 | END | 99 | 102 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 107 | START | 107 | 112 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `2` | `1` | 112 | START | 112 | 161 |
| ✅ EXACT | `Action_BallCarry` | WR | `15` | `14` | 113 | START | 113 | 169 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `10` | `9` | 161 | BOUNDARY | 91 | 161 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `13` | `12` | 161 | BOUNDARY | N/A | 161 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `2` | `1` | 161 | BOUNDARY | 112 | 161 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `5` | `4` | 161 | BOUNDARY | 143 | 161 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `7` | `6` | 161 | BOUNDARY | N/A | 161 |

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
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 106 | 4 | inferred_complete_timeline |
| `Action_Toss` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 176 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_LeadBlock` | 91 | 127 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 88–169
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 88 | 112 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 169 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 115 | 140 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 111 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 112 | 161 | 50 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 161 | 71 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 172 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 138 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 161 | 19 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 144 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 153 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 143 | 163 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 37 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_None` | 114 | 139 | 26 | inferred_complete_timeline |
| `Action_None` | 141 | 169 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 149 | 51 | inferred_complete_timeline |
| `Action_None` | 155 | 179 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 103–170 | 18 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 106–162 | 54 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 143–169 | 27 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 175–239 | 64 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 178–239 | 62 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 179–239 | 59 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 181–216 | 19 | 2 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 188–239 | 52 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 198–235 | 32 | 2 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `13` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [99–102], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=103.
- ⚠️ Action 'Action_None' range [99-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [91-127] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [88-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-118] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-214] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-235] for track '25' has 1 frames without a visible bounding box.
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

</details>