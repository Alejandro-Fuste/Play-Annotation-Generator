# Play-Annotation-Generator Annotation Review — OutsideZoneRead_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_72`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `2` | `2` |
| ⚠️ START CHANGED | `Action_ReadEdgeDefender` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 58 | START | 58 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 58 | START | 58 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 58 | START | 58 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `4` | 58 | START | 58 | 110 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 58 | START | 58 | 110 |
| ✅ EXACT | `Action_PressEdge` | RB | `2` | `2` | 65 | START | 65 | 84 |
| ⚠️ START CHANGED | `Action_ReadEdgeDefender` | Position_Unknown | `18` | `17` | 66 | START | 86 | 86 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 82 | START | 82 | 90 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_Handoff` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_None` | 91 | 359 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PressEdge` | 65 | 84 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 359 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–301
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 110 | 53 | inferred_complete_timeline |
| `Action_None` | 111 | 298 | 188 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 110 | 53 | inferred_complete_timeline |
| `Action_None` | 111 | 251 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 110 | 53 | inferred_complete_timeline |
| `Action_None` | 111 | 126 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 110 | 53 | inferred_complete_timeline |
| `Action_None` | 111 | 280 | 170 | inferred_complete_timeline |
| `Action_None` | 354 | 359 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 110 | 53 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 255 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 65 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 258 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 84 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 156 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 255 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 359 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 359 | 360 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 359 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 76–294 | 219 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 86–359 | 267 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 94–359 | 226 | 8 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 120–359 | 240 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 133–284 | 152 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 141–359 | 217 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 149–350 | 196 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 162–301 | 122 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 169–248 | 80 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 269–359 | 91 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ReadEdgeDefender` for actor_track_id `18` (Position_Unknown): Annotated start 66 != Inferred start 86

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ReadEdgeDefender' for track '17' has invalid range: start=86, end=81. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-255] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [65-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-280] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-128] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-258] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-152] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-310] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-175] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-359] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-196] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-359] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-179] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-343] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-350] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-184] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-200] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-219] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-301] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-248] for track '24' has 1 frames without a visible bounding box.
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