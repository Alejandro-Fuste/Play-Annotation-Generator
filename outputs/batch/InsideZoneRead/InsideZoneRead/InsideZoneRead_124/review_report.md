# Play-Annotation-Generator Annotation Review — InsideZoneRead_124

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_124`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 141 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 142 | START | 142 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 146 | START | 146 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 146 | START | 158 | 192 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 146 | START | 146 | 230 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 146 | START | 146 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 146 | START | 146 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 157 | END | 142 | 157 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `1` | `0` | 159 | START | 159 | 230 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 163 | START | 163 | 174 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 175 | START | 175 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `5` | `4` | 186 | START | 186 | 204 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_SnapReceive` | 142 | 157 | 16 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 175 | 185 | 11 | inferred_complete_timeline |
| `Action_None` | 186 | 216 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 182 | 41 | inferred_complete_timeline |
| `Action_None` | 195 | 272 | 78 | inferred_complete_timeline |
| `Action_None` | 274 | 359 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 158 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 159 | 230 | 72 | inferred_complete_timeline |
| `Action_None` | 240 | 274 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 174 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 230 | 52 | inferred_complete_timeline |
| `Action_None` | 231 | 263 | 33 | inferred_complete_timeline |
| `Action_None` | 302 | 359 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 141 | 112 | inferred_complete_timeline |
| `Action_BallSnap` | 142 | 157 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 192 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 219 | 7 | inferred_complete_timeline |
| `Action_None` | 233 | 262 | 30 | inferred_complete_timeline |
| `Action_None` | 280 | 285 | 6 | inferred_complete_timeline |
| `Action_None` | 290 | 313 | 24 | inferred_complete_timeline |
| `Action_None` | 316 | 333 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 185 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 204 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 227 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 283 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 285 | 292 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 230 | 85 | inferred_complete_timeline |
| `Action_None` | 231 | 253 | 23 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 282 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 292 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 178 | 37 | inferred_complete_timeline |
| `Action_None` | 180 | 202 | 23 | inferred_complete_timeline |
| `Action_None` | 248 | 359 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 40–243
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 141 | 98 | inferred_complete_timeline |
| `Action_None` | 142 | 154 | 13 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 243 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 141 | 67 | inferred_complete_timeline |
| `Action_None` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_None` | 190 | 195 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 213 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–189
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 11 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 105 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 189 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 141 | 35 | inferred_complete_timeline |
| `Action_None` | 142 | 161 | 20 | inferred_complete_timeline |
| `Action_None` | 165 | 183 | 19 | inferred_complete_timeline |
| `Action_None` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_None` | 198 | 233 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_None` | 142 | 159 | 18 | inferred_complete_timeline |
| `Action_None` | 161 | 253 | 93 | inferred_complete_timeline |
| `Action_None` | 259 | 297 | 39 | inferred_complete_timeline |
| `Action_None` | 299 | 327 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 41–43 | 3 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 221–359 | 128 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 224–357 | 122 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 224–359 | 136 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 226–359 | 109 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 250–251 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 253–359 | 107 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 257–359 | 96 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 262–327 | 44 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 281–346 | 59 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 293–315 | 23 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 300–349 | 47 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 317–359 | 30 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 317–343 | 22 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 331–336 | 5 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 332–359 | 9 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 346–359 | 14 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [142–157], lower_priority='Action_ZoneBlock' annotated_start=146, effective_Action_ZoneBlock_start=158.
- ⚠️ Action 'Action_BlockSecondLevel' range [159-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-233] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-327] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-292] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-202] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [158-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-262] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-313] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-213] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-189] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-243] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-352] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-339] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-297] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-303] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-334] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-334] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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