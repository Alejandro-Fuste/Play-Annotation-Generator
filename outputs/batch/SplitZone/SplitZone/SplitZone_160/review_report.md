# Play-Annotation-Generator Annotation Review — SplitZone_160

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_160`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 11 | START | 12 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 11 | START | 12 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 11 | START | 12 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 11 | START | 12 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 11 | START | 12 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 11 | START | 12 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 11 | START | 12 | 83 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 81 | START | 81 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 84 | START | 84 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 84 | START | 101 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `6` | 84 | START | 84 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 84 | START | 84 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `2` | `2` | 87 | START | 87 | 122 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 100 | END | 81 | 100 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `9` | `9` | 124 | START | 124 | 188 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `5` | 128 | START | 128 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 188 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 100 | 20 | inferred_complete_timeline |
| `Action_None` | 101 | 127 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 269 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–176
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 123 | 43 | inferred_complete_timeline |
| `Action_None` | 129 | 157 | 29 | inferred_complete_timeline |
| `Action_None` | 160 | 176 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 86 | 75 | inferred_complete_timeline |
| `Action_SplitBlock` | 87 | 122 | 36 | inferred_complete_timeline |
| `Action_SplitBlock` | 128 | 188 | 61 | inferred_complete_timeline |
| `Action_None` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 83 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 121 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 123 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 124 | 188 | 65 | inferred_complete_timeline |
| `Action_None` | 189 | 263 | 75 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 83 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 140 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 169 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–172
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 100 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 143 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 165 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 172 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–104
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 83 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 101 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–128
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 113 | 33 | inferred_complete_timeline |
| `Action_None` | 118 | 128 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 269 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_None` | 133 | 176 | 44 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–181
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 98 | 140 | 43 | inferred_complete_timeline |
| `Action_None` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 181 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 14–175
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 18 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 52 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 105 | 157 | 53 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–155
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 117 | 37 | inferred_complete_timeline |
| `Action_None` | 140 | 155 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 80 | 69 | inferred_complete_timeline |
| `Action_None` | 81 | 142 | 62 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 156 | 6 | inferred_complete_timeline |
| `Action_None` | 168 | 187 | 20 | inferred_complete_timeline |
| `Action_None` | 193 | 208 | 16 | inferred_complete_timeline |
| `Action_None` | 211 | 243 | 33 | inferred_complete_timeline |
| `Action_None` | 252 | 269 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 12–269 | 243 | 5 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 119–269 | 123 | 9 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 145–269 | 125 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 150–173 | 24 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 162–237 | 48 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 166–181 | 16 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 167–203 | 37 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 322: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 105 frames exceeds threshold 90 frames [start=84, end=188].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [81–100], lower_priority='Action_ZoneBlock' annotated_start=84, effective_Action_ZoneBlock_start=101.
- ⚠️ Action 'Action_None' range [81-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-243] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [87-122] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-140] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-188] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-121] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-263] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-143] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [149-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-148] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-176] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-157] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-234] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>