# Play-Annotation-Generator Annotation Review — JetSweep_115

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_115`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `22` | `20` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `22` | `20` | 39 | START | 121 | 161 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 62 | START | 62 | 72 |
| ✅ EXACT | `Action_LeadBlock` | TE | `5` | `4` | 64 | START | 64 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `9` | 64 | START | 64 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 64 | START | 64 | 122 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 64 | START | 73 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `5` | 64 | START | 64 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 64 | START | 64 | 122 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 72 | END | 62 | 72 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 82 | START | 82 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `2` | `1` | 91 | START | 91 | 257 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 122 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_None` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_Toss` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_None` | 91 | 184 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 140 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 257 | 167 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_LeadBlock` | 64 | 122 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 122 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 122 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 153 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 122 | 50 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 122 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 148 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 122 | 59 | inferred_complete_timeline |
| `Action_None` | 123 | 126 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 81 | 20 | inferred_complete_timeline |
| `Action_None` | 89 | 136 | 48 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–16
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 114 | 53 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 116 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–269 | 266 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 63–155 | 87 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 102–269 | 165 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 121–174 | 43 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 123–189 | 67 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 164–269 | 106 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 170–269 | 100 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 212–269 | 58 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 229–245 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `22` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 64 != Inferred start 73
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [62–72], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=73.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-269] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-114] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-154] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [121-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [173-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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