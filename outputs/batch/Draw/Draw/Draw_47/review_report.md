# Play-Annotation-Generator Annotation Review — Draw_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_47`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `15` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `15` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 61 | START | 61 | 76 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `10` | 64 | START | 77 | 133 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `15` | 64 | START | 64 | 133 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `18` | 64 | START | 64 | 133 |
| ✅ EXACT | `Action_PassBlock` | RG | `22` | `21` | 64 | START | 64 | 133 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `8` | 64 | START | 64 | 133 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 76 | END | 61 | 76 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `14` | `13` | 80 | START | 80 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 110 | START | 110 | 156 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 80 | 109 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 156 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 329 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 115 | 55 | inferred_complete_timeline |
| `Action_None` | 119 | 201 | 83 | inferred_complete_timeline |
| `Action_None` | 203 | 258 | 56 | inferred_complete_timeline |
| `Action_None` | 261 | 316 | 56 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 286 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 284 | 224 | inferred_complete_timeline |
| `Action_None` | 286 | 290 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 133 | 70 | inferred_complete_timeline |
| `Action_None` | 134 | 313 | 180 | inferred_complete_timeline |
| `Action_None` | 315 | 326 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 133 | 70 | inferred_complete_timeline |
| `Action_None` | 134 | 140 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 133 | 57 | inferred_complete_timeline |
| `Action_None` | 134 | 311 | 178 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 133 | 70 | inferred_complete_timeline |
| `Action_None` | 134 | 329 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 133 | 70 | inferred_complete_timeline |
| `Action_None` | 134 | 293 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 100 | 40 | inferred_complete_timeline |
| `Action_None` | 105 | 164 | 60 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 97 | 37 | inferred_complete_timeline |
| `Action_None` | 105 | 311 | 207 | inferred_complete_timeline |
| `Action_None` | 313 | 329 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 158 | 98 | inferred_complete_timeline |
| `Action_None` | 162 | 186 | 25 | inferred_complete_timeline |
| `Action_None` | 190 | 200 | 11 | inferred_complete_timeline |
| `Action_None` | 205 | 317 | 113 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 329 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 286 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 300 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 106 | 46 | inferred_complete_timeline |
| `Action_None` | 108 | 156 | 49 | inferred_complete_timeline |
| `Action_None` | 158 | 167 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 184 | 14 | inferred_complete_timeline |
| `Action_None` | 188 | 193 | 6 | inferred_complete_timeline |
| `Action_None` | 196 | 301 | 106 | inferred_complete_timeline |
| `Action_None` | 304 | 329 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 281 | 221 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 113–114 | 2 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 135–141 | 7 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 153–311 | 155 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 320–322 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 64 != Inferred start 77
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [61–76], lower_priority='Action_PassBlock' annotated_start=64, effective_Action_PassBlock_start=77.
- ⚠️ Action 'Action_None' range [61-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-158] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-317] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-311] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-156] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-167] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-301] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-293] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-311] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-300] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-286] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-313] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-326] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-281] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-258] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-316] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-311] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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