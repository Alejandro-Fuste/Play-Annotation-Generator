# Play-Annotation-Generator Annotation Review — Counter_343

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_343`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LT | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `19` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `22` | `21` | 138 | START | 138 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `18` | `17` | 141 | START | 141 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 141 | START | 141 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 141 | START | 151 | 220 |
| ✅ EXACT | `Action_PullBlock` | LG | `8` | `7` | 141 | START | 141 | 184 |
| ✅ EXACT | `Action_PullLeadBlock` | TE1 | `19` | `18` | 141 | START | 141 | 236 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 150 | END | 138 | 150 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 166 | START | 166 | 183 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LT | `7` | `6` | 184 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 236 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_None` | 151 | 165 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 166 | 183 | 18 | inferred_complete_timeline |
| `Action_None` | 184 | 316 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 359 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 359 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 141 | 236 | 96 | inferred_complete_timeline |
| `Action_None` | 237 | 322 | 86 | inferred_complete_timeline |
| `Action_None` | 324 | 359 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 166 | 29 | inferred_complete_timeline |
| `Action_None` | 168 | 247 | 80 | inferred_complete_timeline |
| `Action_None` | 249 | 352 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 178 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PullBlock` | 141 | 184 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_BallSnap` | 138 | 146 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 151 | 220 | 70 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 236 | 15 | inferred_complete_timeline |
| `Action_None` | 237 | 348 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 195 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 236 | 40 | inferred_complete_timeline |
| `Action_None` | 237 | 359 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 157 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 219 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 224 | 236 | 13 | inferred_complete_timeline |
| `Action_None` | 237 | 359 | 123 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 234 | 97 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 247 | 359 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 184 | 47 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 233 | 42 | inferred_complete_timeline |
| `Action_None` | 235 | 263 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 339 | 202 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 345 | 208 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 201 | 64 | inferred_complete_timeline |
| `Action_None` | 217 | 347 | 131 | inferred_complete_timeline |
| `Action_None` | 349 | 351 | 3 | inferred_complete_timeline |
| `Action_None` | 353 | 359 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 161 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 222 | 85 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 359 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 359 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 280 | 143 | inferred_complete_timeline |
| `Action_None` | 283 | 359 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 312 | 175 | inferred_complete_timeline |
| `Action_None` | 314 | 359 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 301 | 164 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 359 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–359 | 358 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 148–196 | 4 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 152–195 | 18 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 190–359 | 170 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 193–359 | 167 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 202–359 | 152 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 242–246 | 5 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 266–325 | 43 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 289–355 | 67 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `7` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 688: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '6' has invalid range: start=184, end=178. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (RT) duration 96 frames exceeds threshold 90 frames [start=141, end=236].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 96 frames exceeds threshold 90 frames [start=141, end=236].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (C) duration 96 frames exceeds threshold 90 frames [start=141, end=236].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [138–150], lower_priority='Action_DownBlock' annotated_start=141, effective_Action_DownBlock_start=151.
- ⚠️ Action 'Action_None' range [138-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-347] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-234] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-345] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-178] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [141-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-312] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-339] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-316] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-263] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-166] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-247] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-352] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-219] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [141-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-322] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-359] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-195] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [138-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [151-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-348] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-359] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-282] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-316] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-355] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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