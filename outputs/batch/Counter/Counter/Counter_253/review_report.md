# Play-Annotation-Generator Annotation Review — Counter_253

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_253`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 56
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | offense | `7` | `6` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB1 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | RB2 | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `5` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `7` | `Group` | 0 | START | 0 | 170 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 168 | START | 168 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 171 | START | 188 | 197 |
| ✅ EXACT | `Action_DownBlock` | RT | `18` | `17` | 171 | START | 171 | 258 |
| ✅ EXACT | `Action_PullBlock` | RG | `22` | `21` | 171 | START | 171 | 258 |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | `7` | `6` | 171 | START | 171 | 245 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB1 | `5` | `4` | 175 | START | 175 | 338 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `19` | `18` | 187 | START | 187 | 212 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `19` | `18` | 187 | END | N/A | N/A |
| ✅ EXACT | `Action_BallCarry` | RB2 | `7` | `6` | 246 | START | 246 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 258 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_Handoff` | 187 | 212 | 26 | inferred_complete_timeline |
| `Action_Handoff` | 215 | 245 | 31 | inferred_complete_timeline |
| `Action_None` | 246 | 333 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–338
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 175 | 338 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 171 | 245 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 359 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 227 | 60 | inferred_complete_timeline |
| `Action_None` | 252 | 349 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 352 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 194 | 27 | inferred_complete_timeline |
| `Action_None` | 204 | 224 | 21 | inferred_complete_timeline |
| `Action_None` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 355 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_BallSnap` | 168 | 187 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 197 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PullBlock` | 171 | 258 | 88 | inferred_complete_timeline |
| `Action_None` | 259 | 344 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 258 | 88 | inferred_complete_timeline |
| `Action_None` | 259 | 359 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 209 | 42 | inferred_complete_timeline |
| `Action_None` | 213 | 233 | 21 | inferred_complete_timeline |
| `Action_None` | 250 | 252 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 254 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 274 | 107 | inferred_complete_timeline |
| `Action_None` | 280 | 359 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 222 | 55 | inferred_complete_timeline |
| `Action_None` | 225 | 240 | 16 | inferred_complete_timeline |
| `Action_None` | 249 | 359 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 200 | 33 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 355 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 287 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 356 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_None` | 168 | 359 | 192 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–261 | 262 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 43–48 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 248–251 | 4 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 255–359 | 103 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 256–359 | 99 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 281–359 | 64 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 328–359 | 32 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 353–359 | 7 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `19` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 34 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 508: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [168–187], lower_priority='Action_DownBlock' annotated_start=171, effective_Action_DownBlock_start=188.
- ⚠️ Overlapping action conflict at frame 187 for track '18': 'Action_SnapReceive' vs 'Action_Handoff'. Overriding with 'Action_Handoff'.
- ⚠️ Action 'Action_None' range [168-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [175-338] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-209] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-233] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-355] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-352] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [188-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-349] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-240] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [187-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-333] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-356] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-355] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-344] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-275] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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