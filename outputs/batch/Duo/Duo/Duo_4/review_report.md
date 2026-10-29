# Play-Annotation-Generator Annotation Review — Duo_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_4`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `24` | `21` |
| ✅ EXACT | `Action_ComboBlock` | TE2 | offense | `3` | `3` |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | defense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `24` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 302 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 96 |
| ✅ EXACT | `Action_ComboBlock` | RG | `10` | `10` | 210 | START | 210 | 277 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `24` | `21` | 210 | START | 210 | 238 |
| ✅ EXACT | `Action_ComboBlock` | TE2 | `3` | `3` | 210 | START | 210 | 277 |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | `9` | `9` | 210 | START | 210 | 277 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 237 | START | 237 | 305 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `24` | `21` | 239 | START | 239 | 277 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 277 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 305 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 308 | 328 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ComboBlock` | 210 | 277 | 68 | inferred_complete_timeline |
| `Action_None` | 278 | 328 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 328 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ComboBlock` | 210 | 277 | 68 | inferred_complete_timeline |
| `Action_None` | 278 | 298 | 21 | inferred_complete_timeline |
| `Action_None` | 300 | 306 | 7 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 309 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 328 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 328 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 150 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 244 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 328 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_ComboBlock` | 210 | 277 | 68 | inferred_complete_timeline |
| `Action_None` | 278 | 328 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–208 | 156 | 12 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 67–317 | 248 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 95–328 | 223 | 6 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 121–175 | 54 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 202–328 | 127 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 236–315 | 78 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 246–327 | 78 | 3 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 304–328 | 23 | 2 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 304–328 | 25 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 310–313 | 4 | 1 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 321–324 | 4 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 328–328 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 10: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-328] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-255] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-328] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [210-277] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-305] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-298] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-150] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-309] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-142] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-308] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-284] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-294] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-313] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [239-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-328] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-296] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-315] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-254] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-327] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-308] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-324] for track '29' has 1 frames without a visible bounding box.
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

</details>