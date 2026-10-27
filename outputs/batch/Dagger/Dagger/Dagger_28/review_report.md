# Play-Annotation-Generator Annotation Review — Dagger_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_28`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 389
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | OLB | defense | `3` | `3` |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 89 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 163 | START | 163 | 165 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 166 | START | 166 | 167 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 166 | START | 166 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 166 | START | 171 | 174 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 166 | START | 166 | 167 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | `21` | `21` | 166 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 167 | END | 164 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | OLB | `3` | `3` | 182 | START | 182 | 219 |
| ✅ EXACT | `Action_ClearToEdge` | WR2 | `2` | `2` | 182 | START | 182 | 194 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `17` | `17` | 270 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 179 | 12 | inferred_complete_timeline |
| `Action_None` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 227 | 65 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_ClearToEdge` | 182 | 194 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 259 | 97 | inferred_complete_timeline |
| `Action_None` | 261 | 267 | 7 | inferred_complete_timeline |
| `Action_None` | 270 | 274 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 177 | 15 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 212 | 242 | 31 | inferred_complete_timeline |
| `Action_None` | 285 | 288 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_BallSnap` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 192 | 194 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 117 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 166 | 172 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 389 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 211 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 380 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_BreakInside` | 182 | 219 | 38 | inferred_complete_timeline |
| `Action_BreakInside` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_BreakInside` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_BreakInside` | 235 | 244 | 10 | inferred_complete_timeline |
| `Action_BreakInside` | 246 | 267 | 22 | inferred_complete_timeline |
| `Action_BreakInside` | 272 | 273 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 389 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 345 | 183 | inferred_complete_timeline |
| `Action_None` | 347 | 361 | 15 | inferred_complete_timeline |
| `Action_None` | 363 | 389 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 350 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 206–237 | 31 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 208–271 | 64 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 222–311 | 42 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 247–273 | 21 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 254–371 | 117 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 281–282 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 281–300 | 16 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 283–289 | 7 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 287–293 | 7 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 292–335 | 43 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 323–372 | 49 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 324–325 | 2 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 336–351 | 8 | 3 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 361–366 | 6 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 371–375 | 5 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 379–389 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `21` (LG)
- ⚠️ Ambiguous match for action `Action_BreakInside` and target `3` (6 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `17` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '17' has invalid range: start=270, end=188. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [163–167], lower_priority='Action_PassBlock' annotated_start=166, effective_Action_PassBlock_start=168.
- ⚠️ Segment 'Action_PassBlock' for track '21' has invalid range: start=166, end=121. Clamping end to start.
- ⚠️ Action 'Action_None' range [163-259] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [182-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [182-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [221-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [228-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [235-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [246-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [272-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-389] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-350] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-345] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-361] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-98] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-99] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-130] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-141] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-179] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [163-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-174] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [192-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [166-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-273] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-371] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-294] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-293] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-361] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-372] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-366] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>