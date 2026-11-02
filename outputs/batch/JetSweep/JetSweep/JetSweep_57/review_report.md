# Play-Annotation-Generator Annotation Review — JetSweep_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_57`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_BlockSecondLevel` | OLB2 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `17` | `16` | 40 | START | 40 | 70 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `13` | `12` | 48 | START | 49 | 60 |
| ✅ EXACT | `Action_LeadBlock` | RB | `3` | `2` | 55 | START | 55 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 55 | START | 55 | 110 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 55 | START | 61 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 55 | START | 55 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `4` | 55 | START | 55 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 55 | START | 55 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 60 | END | 48 | 60 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 68 | START | 68 | 72 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `17` | `16` | 73 | START | 73 | 216 |
| ✅ EXACT | `Action_BlockSecondLevel` | OLB2 | `8` | `7` | 88 | START | 88 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 60 | 13 | inferred_complete_timeline |
| `Action_None` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_Toss` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 73 | 143 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_LeadBlock` | 55 | 94 | 40 | inferred_complete_timeline |
| `Action_None` | 113 | 124 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 133 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 110 | 56 | inferred_complete_timeline |
| `Action_None` | 111 | 141 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 101 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 111 | 138 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 110 | 50 | inferred_complete_timeline |
| `Action_None` | 111 | 188 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 110 | 56 | inferred_complete_timeline |
| `Action_None` | 111 | 173 | 63 | inferred_complete_timeline |
| `Action_None` | 176 | 184 | 9 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 226 | 14 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 110 | 56 | inferred_complete_timeline |
| `Action_None` | 111 | 235 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 78 | 31 | inferred_complete_timeline |
| `Action_None` | 96 | 130 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 239 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 99 | 52 | inferred_complete_timeline |
| `Action_None` | 103 | 239 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 174 | 127 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 117 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 88 | 110 | 23 | inferred_complete_timeline |
| `Action_None` | 111 | 239 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 92 | 45 | inferred_complete_timeline |
| `Action_None` | 97 | 206 | 110 | inferred_complete_timeline |
| `Action_None` | 208 | 214 | 7 | inferred_complete_timeline |
| `Action_None` | 216 | 220 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 40–216 | 176 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 70–150 | 81 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 122–152 | 30 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 124–239 | 116 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 126–161 | 31 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–239 | 113 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 129–176 | 46 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 142–224 | 83 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 158–219 | 58 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 161–186 | 12 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 177–239 | 63 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 202–239 | 36 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 228–230 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `17` (2 segments found)
- ⚠️ `Action_BallSnap` for actor_track_id `13` (C): Annotated start 48 != Inferred start 49
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 55 != Inferred start 61
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [48–60], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=61.
- ⚠️ Action 'Action_None' range [111-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [55-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-206] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [88-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-117] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [40-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-171] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-219] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-236] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '29' has 1 frames without a visible bounding box.
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

</details>