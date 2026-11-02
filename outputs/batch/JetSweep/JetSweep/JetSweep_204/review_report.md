# Play-Annotation-Generator Annotation Review — JetSweep_204

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_204`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `3` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `6` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 92 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `3` | 81 | START | 81 | 95 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `18` | `16` | 81 | START | 85 | 109 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `5` | `4` | 93 | START | 93 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 93 | START | 93 | 170 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 93 | START | 93 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `3` | 93 | START | 96 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 93 | START | 93 | 170 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 93 | START | 93 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 95 | END | 81 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 106 | START | 106 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `16` | 110 | START | 110 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_Toss` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 161 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_LeadBlock` | 93 | 122 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 130 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 170 | 78 | inferred_complete_timeline |
| `Action_None` | 171 | 239 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 170 | 78 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 152 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 150 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 145 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 131 | 30 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 12 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 25 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 92 | 12 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |
| `Action_None` | 112 | 166 | 55 | inferred_complete_timeline |
| `Action_None` | 170 | 183 | 14 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 148 | 68 | inferred_complete_timeline |
| `Action_None` | 150 | 239 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 161 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 147 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 85–236 | 151 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 91–191 | 98 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 120–176 | 57 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 133–239 | 107 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 135–239 | 105 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 138–148 | 7 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 144–174 | 31 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 157–171 | 15 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 160–239 | 79 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 168–237 | 61 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 171–239 | 69 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `18` (Position_Unknown): Annotated start 81 != Inferred start 85
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 410: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [81–95], lower_priority='Action_ZoneBlock' annotated_start=93, effective_Action_ZoneBlock_start=96.
- ⚠️ Action 'Action_ZoneBlock' range [93-145] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [93-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-147] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-60] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-25] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-217] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-236] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-222] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
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

</details>