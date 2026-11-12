# Play-Annotation-Generator Annotation Review — SplitZone_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_111`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 10
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 8 | START | 9 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 8 | START | 9 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 8 | START | 9 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 8 | START | 9 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 8 | START | 9 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 8 | START | 9 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 8 | START | 9 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 8 | START | 9 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 8 | START | 9 | 97 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 95 | START | 95 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 98 | START | 98 | 189 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 98 | START | 98 | 189 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `21` | 98 | START | 110 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 98 | START | 98 | 121 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 98 | START | 98 | 189 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `2` | `2` | 101 | START | 101 | 189 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 109 | END | 95 | 109 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `20` | 113 | START | 113 | 119 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 120 | START | 120 | 299 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `21` | `21` | 122 | START | 122 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 189 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–295
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_None` | 120 | 295 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 119 | 111 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 299 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–121
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 97 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 121 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 97 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 189 | 92 | inferred_complete_timeline |
| `Action_None` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_None` | 209 | 299 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 95 | 109 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 122 | 186 | 65 | inferred_complete_timeline |
| `Action_None` | 196 | 205 | 10 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 97 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 189 | 92 | inferred_complete_timeline |
| `Action_None` | 190 | 299 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 97 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 189 | 92 | inferred_complete_timeline |
| `Action_None` | 190 | 299 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 157 | 63 | inferred_complete_timeline |
| `Action_None` | 162 | 202 | 41 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 123 | 29 | inferred_complete_timeline |
| `Action_None` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_None` | 146 | 299 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–149
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 149 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–161
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 151 | 57 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 219 | 125 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 9–293
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 94 | 86 | inferred_complete_timeline |
| `Action_None` | 95 | 293 | 199 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 9–293 | 281 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 9–299 | 291 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 11–29 | 7 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 133–299 | 167 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 163–166 | 4 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 174–299 | 124 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 180–184 | 5 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 182–299 | 118 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 190–193 | 4 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 261–268 | 8 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 278–289 | 7 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 98 != Inferred start 110

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 224: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 224: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 92 frames exceeds threshold 90 frames [start=98, end=189].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 92 frames exceeds threshold 90 frames [start=98, end=189].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 92 frames exceeds threshold 90 frames [start=98, end=189].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [95–109], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=110.
- ⚠️ Action 'Action_None' range [95-283] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-189] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [122-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-14] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>