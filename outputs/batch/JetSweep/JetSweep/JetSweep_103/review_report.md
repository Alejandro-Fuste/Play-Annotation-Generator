# Play-Annotation-Generator Annotation Review — JetSweep_103

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_103`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `15` | `14` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Toss` | QB | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR3 | offense | `15` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 151 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `15` | `14` | 131 | START | 131 | 139 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 149 | START | 149 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `3` | `2` | 152 | START | 152 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 152 | START | 152 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 152 | START | 152 | 216 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 152 | START | 152 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 152 | START | 161 | 162 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 152 | START | 152 | 179 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 160 | END | 149 | 160 |
| ✅ EXACT | `Action_Toss` | QB | `7` | `6` | 165 | START | 165 | 179 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR3 | `15` | `14` | 180 | START | N/A | N/A |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `8` | `7` | 180 | START | 180 | 229 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 229 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_SnapReceive` | 149 | 160 | 12 | inferred_complete_timeline |
| `Action_None` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_Toss` | 165 | 179 | 15 | inferred_complete_timeline |
| `Action_None` | 180 | 235 | 56 | inferred_complete_timeline |
| `Action_None` | 309 | 359 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 165 | 17 | inferred_complete_timeline |
| `Action_None` | 167 | 196 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 184 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 307 | 159 | inferred_complete_timeline |
| `Action_None` | 311 | 338 | 28 | inferred_complete_timeline |
| `Action_None` | 342 | 351 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 130 | 29 | inferred_complete_timeline |
| `Action_JetMotion` | 131 | 139 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_LeadBlock` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_LeadBlock` | 176 | 229 | 54 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |
| `Action_None` | 244 | 295 | 52 | inferred_complete_timeline |
| `Action_None` | 297 | 359 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 207 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 216 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 148 | 93 | inferred_complete_timeline |
| `Action_BallSnap` | 149 | 160 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 229 | 48 | inferred_complete_timeline |
| `Action_None` | 230 | 359 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 229 | 78 | inferred_complete_timeline |
| `Action_None` | 230 | 254 | 25 | inferred_complete_timeline |
| `Action_None` | 261 | 305 | 45 | inferred_complete_timeline |
| `Action_None` | 312 | 359 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 179 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 180 | 229 | 50 | inferred_complete_timeline |
| `Action_None` | 230 | 359 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 213 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 359 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 359 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 261 | 113 | inferred_complete_timeline |
| `Action_None` | 263 | 290 | 28 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 359 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 232 | 84 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 195 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 188 | 40 | inferred_complete_timeline |
| `Action_None` | 190 | 216 | 27 | inferred_complete_timeline |
| `Action_None` | 218 | 359 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 220 | 72 | inferred_complete_timeline |
| `Action_None` | 222 | 295 | 74 | inferred_complete_timeline |
| `Action_None` | 297 | 336 | 40 | inferred_complete_timeline |
| `Action_None` | 339 | 359 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 194 | 46 | inferred_complete_timeline |
| `Action_None` | 197 | 299 | 103 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 359 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 140–350 | 204 | 7 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 215–359 | 142 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 243–347 | 105 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 279–357 | 75 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 281–355 | 75 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 295–336 | 39 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 299–359 | 61 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 301–359 | 59 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 319–359 | 41 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 348–359 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `15` (WR3)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '14' has invalid range: start=180, end=139. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [149–160], lower_priority='Action_ZoneBlock' annotated_start=152, effective_Action_ZoneBlock_start=161.
- ⚠️ Action 'Action_None' range [149-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-295] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-336] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [152-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [176-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-295] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-290] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-307] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-338] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-351] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-254] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-305] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [152-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [131-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-299] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-359] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-148] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-359] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-290] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-350] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-307] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-347] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-344] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-355] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-336] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-353] for track '29' has 1 frames without a visible bounding box.
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