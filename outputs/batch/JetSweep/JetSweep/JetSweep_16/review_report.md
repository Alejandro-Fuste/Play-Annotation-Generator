# Play-Annotation-Generator Annotation Review — JetSweep_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_16`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | WR | offense | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `19` | `18` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `1` | `0` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `18` | `17` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 71 |
| ⚠️ START CHANGED | `Action_JetMotion` | WR | `19` | `18` | 10 | START | 70 | 76 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 72 | START | 72 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `19` | `18` | 77 | START | 77 | 95 |
| ✅ EXACT | `Action_LeadBlock` | TE | `3` | `2` | 78 | START | 78 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 78 | START | 78 | 95 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 78 | START | 78 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 78 | START | 100 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 78 | START | 78 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `5` | 78 | START | 78 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 85 | END | 72 | 85 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 92 | START | 92 | 160 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `1` | `0` | 140 | BOUNDARY | 98 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `11` | `10` | 140 | BOUNDARY | 78 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `18` | `17` | 140 | BOUNDARY | 105 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `2` | `1` | 140 | BOUNDARY | 78 | 140 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `6` | `5` | 140 | BOUNDARY | 103 | 140 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 72 | 85 | 14 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_Toss` | 92 | 160 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 105 | 34 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 70–217
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 95 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 198 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 217 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_LeadBlock` | 78 | 90 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 102 | 31 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 140 | 63 | inferred_complete_timeline |
| `Action_None` | 141 | 212 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 92 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 140 | 38 | inferred_complete_timeline |
| `Action_None` | 141 | 206 | 66 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 16 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 71 | 53 | inferred_complete_timeline |
| `Action_BallSnap` | 72 | 82 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 140 | 36 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 95 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 140 | 43 | inferred_complete_timeline |
| `Action_None` | 141 | 165 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 140 | 63 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_None` | 78 | 116 | 39 | inferred_complete_timeline |
| `Action_None` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_None` | 148 | 163 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 71 | 48 | inferred_complete_timeline |
| `Action_None` | 72 | 196 | 125 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–33
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 33 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 227 | 156 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 94 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 71 | 1 | inferred_complete_timeline |
| `Action_None` | 72 | 213 | 142 | inferred_complete_timeline |
| `Action_None` | 218 | 223 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 178 | 107 | inferred_complete_timeline |
| `Action_None` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `23` | Position_Unknown | Team_Unknown | 101–239 | 135 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 119–239 | 93 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 125–239 | 115 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 129–228 | 100 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 136–140 | 5 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 137–142 | 6 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 170–174 | 5 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 171–239 | 69 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 176–239 | 64 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 178–223 | 46 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `19` (WR): Annotated start 10 != Inferred start 70
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [72–85], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=86.
- ⚠️ Action 'Action_ZoneBlock' range [78-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-165] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [78-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-213] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [92-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-196] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [72-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-198] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-239] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-223] for track '28' has 1 frames without a visible bounding box.
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

</details>