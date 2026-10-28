# Play-Annotation-Generator Annotation Review — Draw_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_26`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `12` | `11` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `12` | `11` | 43 | START | 43 | 57 |
| ✅ EXACT | `Action_PassBlock` | LT | `1` | `0` | 46 | START | 46 | 180 |
| ✅ EXACT | `Action_PassBlock` | RG | `14` | `13` | 46 | START | 46 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `3` | `2` | 46 | START | 46 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `3` | 46 | START | 46 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 57 | END | 43 | 57 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `13` | `12` | 61 | START | 61 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 90 | START | 90 | 187 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 180 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 61 | 89 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 187 | 98 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 85 | 43 | inferred_complete_timeline |
| `Action_None` | 91 | 198 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 180 | 135 | inferred_complete_timeline |
| `Action_None` | 181 | 381 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 152 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 180 | 27 | inferred_complete_timeline |
| `Action_None` | 181 | 201 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 172 | 127 | inferred_complete_timeline |
| `Action_None` | 252 | 312 | 61 | inferred_complete_timeline |
| `Action_None` | 314 | 361 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 97 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 180 | 76 | inferred_complete_timeline |
| `Action_None` | 181 | 300 | 120 | inferred_complete_timeline |
| `Action_None` | 302 | 308 | 7 | inferred_complete_timeline |
| `Action_None` | 311 | 319 | 9 | inferred_complete_timeline |
| `Action_None` | 326 | 340 | 15 | inferred_complete_timeline |
| `Action_None` | 347 | 350 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 242 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 147 | 105 | inferred_complete_timeline |
| `Action_None` | 189 | 252 | 64 | inferred_complete_timeline |
| `Action_None` | 255 | 354 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_None` | 58 | 77 | 20 | inferred_complete_timeline |
| `Action_None` | 79 | 161 | 83 | inferred_complete_timeline |
| `Action_None` | 163 | 228 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–401
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 327 | 285 | inferred_complete_timeline |
| `Action_None` | 334 | 401 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 95 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 117 | 75 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 78 | 36 | inferred_complete_timeline |
| `Action_None` | 83 | 177 | 95 | inferred_complete_timeline |
| `Action_None` | 179 | 200 | 22 | inferred_complete_timeline |
| `Action_None` | 245 | 365 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 5–54 | 44 | 4 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 61–86 | 23 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 120–211 | 82 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 133–163 | 31 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 154–200 | 43 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 169–449 | 271 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 177–223 | 22 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 192–449 | 245 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 195–449 | 244 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 207–396 | 190 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 209–301 | 90 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 218–449 | 231 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 219–229 | 10 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 233–373 | 137 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 252–263 | 12 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 256–449 | 177 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 267–272 | 6 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 270–397 | 125 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 273–352 | 80 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 277–337 | 61 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 279–449 | 149 | 6 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 295–323 | 24 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 296–449 | 154 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 337–449 | 100 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 92 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_None' range [181-381] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-152] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-340] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-327] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-401] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-252] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-354] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-198] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-117] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-177] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-365] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-161] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [61-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-187] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-239] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-172] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-312] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-361] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-9] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-196] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-233] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-280] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-364] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-315] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-328] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-396] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-301] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-373] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-263] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-295] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-368] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-383] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-449] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-397] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-352] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-337] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-376] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-406] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-421] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-314] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-423] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-449] for track '38' has 1 frames without a visible bounding box.
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

</details>