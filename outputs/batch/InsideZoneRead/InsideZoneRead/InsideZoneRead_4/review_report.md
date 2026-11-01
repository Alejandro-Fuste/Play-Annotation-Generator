# Play-Annotation-Generator Annotation Review — InsideZoneRead_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_4`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 61
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 6 | START | 6 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 6 | START | 6 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 6 | START | 6 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 6 | START | 6 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 6 | START | 6 | 124 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 86 | START | 86 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 88 | START | 88 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 88 | START | 88 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `4` | 88 | START | 100 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `5` | 88 | START | 88 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 88 | START | 88 | 168 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 99 | END | 86 | 99 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `10` | 104 | START | 104 | 113 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 114 | START | 114 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 125 | START | 125 | 192 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `2` | `1` | 127 | START | 127 | 171 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 171 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–237
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 124 | 11 | inferred_complete_timeline |
| `Action_None` | 125 | 227 | 103 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–223
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 124 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 192 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 202 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 223 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 6–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 87 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 126 | 39 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 127 | 171 | 45 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 6–181
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 87 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 171 | 66 | inferred_complete_timeline |
| `Action_None` | 172 | 181 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–173
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 171 | 72 | inferred_complete_timeline |
| `Action_None` | 172 | 173 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–171
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 87 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 122 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 171 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 87 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 168 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–209
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 153 | 68 | inferred_complete_timeline |
| `Action_None` | 158 | 209 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–161
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 161 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–177
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 177 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–136
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 136 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 214 | 129 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 101 | 16 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 24–93 | 69 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 148–159 | 8 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 169–175 | 7 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 178–239 | 57 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 204–239 | 36 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | 117 | 120 | 4 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [86–99], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=100.
- ⚠️ Action 'Action_ZoneBlock' range [88-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-214] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [195-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-177] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>