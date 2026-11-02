# Play-Annotation-Generator Annotation Review — JetSweep_222

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_222`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Toss` | QB | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_BallSnap` | RG | `8` | `7` | 58 | START | 58 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | `4` | `3` | 59 | START | 59 | 70 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 59 | START | 59 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 59 | START | 59 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `17` | 59 | START | 59 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 59 | START | 59 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 59 | START | 59 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `20` | `19` | 65 | START | 66 | 80 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 65 | END | 58 | 65 |
| ✅ EXACT | `Action_Toss` | QB | `6` | `5` | 83 | START | 83 | 86 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `20` | `19` | 87 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 117 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_None` | 66 | 82 | 17 | inferred_complete_timeline |
| `Action_Toss` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 154 | 68 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 115 | 58 | inferred_complete_timeline |
| `Action_None` | 118 | 150 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_None` | 161 | 166 | 6 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_LeadBlock` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 85 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 116 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 116 | 58 | inferred_complete_timeline |
| `Action_None` | 120 | 153 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 117 | 59 | inferred_complete_timeline |
| `Action_None` | 118 | 154 | 37 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 117 | 59 | inferred_complete_timeline |
| `Action_None` | 118 | 153 | 36 | inferred_complete_timeline |
| `Action_None` | 160 | 172 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 117 | 59 | inferred_complete_timeline |
| `Action_None` | 118 | 153 | 36 | inferred_complete_timeline |
| `Action_None` | 159 | 210 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 117 | 59 | inferred_complete_timeline |
| `Action_None` | 118 | 128 | 11 | inferred_complete_timeline |
| `Action_None` | 163 | 194 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 157 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 119 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 94 | 110 | 17 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 153 | 18 | inferred_complete_timeline |
| `Action_None` | 164 | 174 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 102 | 45 | inferred_complete_timeline |
| `Action_None` | 161 | 172 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 105 | 48 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 166 | 210 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 137 | 80 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 210 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 135 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–76 | 77 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 66–84 | 18 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 67–102 | 36 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 97–118 | 22 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 120–171 | 9 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 131–161 | 25 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 132–210 | 55 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 162–190 | 29 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 163–210 | 47 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 167–210 | 20 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 167–184 | 18 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 167–210 | 44 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 175–210 | 32 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 177–209 | 33 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 178–198 | 19 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 178–210 | 29 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 181–183 | 3 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 192–205 | 14 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 194–208 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `20` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 446: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '19' has invalid range: start=87, end=84. Clamping end to start.
- ⚠️ Action 'Action_None' range [118-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-105] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [59-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [79-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [66-80] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [82-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-190] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-186] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-209] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-186] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-205] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>