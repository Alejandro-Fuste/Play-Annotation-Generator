# Play-Annotation-Generator Annotation Review — Counter_243

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_243`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RG | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 176 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 177 | START | 177 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `17` | `16` | 181 | START | 181 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `20` | `19` | 181 | START | 181 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 181 | START | 192 | 197 |
| ✅ EXACT | `Action_PullBlock` | LG | `19` | `18` | 181 | START | 181 | 224 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `4` | `3` | 181 | START | 181 | 264 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `10` | `9` | 191 | END | 177 | 191 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `10` | `9` | 210 | START | 210 | 220 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RG | `22` | `21` | 221 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 327 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 199 | 23 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |
| `Action_None` | 281 | 420 | 140 | inferred_complete_timeline |
| `Action_None` | 422 | 449 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 224 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_BallSnap` | 177 | 191 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 264 | 60 | inferred_complete_timeline |
| `Action_None` | 265 | 449 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 206 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 208 | 233 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 326 | 150 | inferred_complete_timeline |
| `Action_None` | 412 | 449 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 286 | 110 | inferred_complete_timeline |
| `Action_None` | 291 | 449 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 264 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 449 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_None` | 177 | 434 | 258 | inferred_complete_timeline |
| `Action_None` | 438 | 439 | 2 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–449 | 445 | 4 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–449 | 450 | 3 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–257 | 248 | 4 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–449 | 450 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–211 | 208 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 221–318 | 95 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 231–236 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 238–449 | 212 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 263–449 | 187 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 263–399 | 128 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 263–295 | 28 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 264–280 | 12 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 282–449 | 168 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 304–412 | 107 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 328–449 | 122 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 334–449 | 116 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 341–449 | 109 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 391–449 | 28 | 8 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 410–449 | 29 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 431–432 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `22` (RG)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 487: Duplicate assignment for track ID '22' in grid. Overwriting previous assignment.
- ⚠️ Row 487: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 488: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 488: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [177–191], lower_priority='Action_DownBlock' annotated_start=181, effective_Action_DownBlock_start=192.
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=221, end=211. Clamping end to start.
- ⚠️ Action 'Action_None' range [177-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [181-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-252] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-434] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-327] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-326] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [208-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [236-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-199] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-420] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [181-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-194] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-204] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-211] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-312] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-340] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-399] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-273] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-412] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-449] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-402] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-435] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-427] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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