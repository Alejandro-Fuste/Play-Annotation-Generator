# Play-Annotation-Generator Annotation Review — Counter_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_31`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 52
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | HB | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 224 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `7` | `Group` | 0 | START | 0 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 200 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 201 | START | 201 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 207 | START | 233 | 236 |
| ✅ EXACT | `Action_DownBlock` | RG | `20` | `19` | 207 | START | 207 | 287 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 207 | START | 207 | 287 |
| ✅ EXACT | `Action_PullLeadBlock` | HB | `7` | `6` | 207 | START | 207 | 287 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 225 | END | 201 | 225 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 232 | START | 232 | 244 |
| ✅ EXACT | `Action_BallCarry` | RB | `16` | `15` | 245 | START | 245 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 287 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_SnapReceive` | 201 | 225 | 25 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 232 | 244 | 13 | inferred_complete_timeline |
| `Action_None` | 245 | 366 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 244 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 389 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 207 | 287 | 81 | inferred_complete_timeline |
| `Action_None` | 288 | 389 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 389 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 389 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 381 | 181 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 233 | 33 | inferred_complete_timeline |
| `Action_None` | 235 | 294 | 60 | inferred_complete_timeline |
| `Action_None` | 297 | 307 | 11 | inferred_complete_timeline |
| `Action_None` | 310 | 389 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PullBlock` | 207 | 287 | 81 | inferred_complete_timeline |
| `Action_None` | 288 | 368 | 81 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_BallSnap` | 201 | 222 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 240 | 241 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 287 | 81 | inferred_complete_timeline |
| `Action_None` | 288 | 389 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 389 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 240 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 262 | 62 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 271 | 389 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 252 | 52 | inferred_complete_timeline |
| `Action_None` | 273 | 389 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 253 | 53 | inferred_complete_timeline |
| `Action_None` | 256 | 389 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 331 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 280 | 80 | inferred_complete_timeline |
| `Action_None` | 283 | 389 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 285 | 85 | inferred_complete_timeline |
| `Action_None` | 288 | 389 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 389 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 389 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 389 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 307 | 107 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 214–240 | 10 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 237–272 | 26 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 264–389 | 118 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 272–389 | 116 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 305–389 | 85 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 356–389 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [201–225], lower_priority='Action_DownBlock' annotated_start=207, effective_Action_DownBlock_start=226.
- ⚠️ Action 'Action_None' range [201-381] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-262] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-307] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-285] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [201-222] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [233-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [240-241] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-307] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-287] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-366] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [207-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-368] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-297] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-348] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-349] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-389] for track '27' has 1 frames without a visible bounding box.
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

</details>