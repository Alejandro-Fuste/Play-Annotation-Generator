# Play-Annotation-Generator Annotation Review — Counter_268

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_268`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 145
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `19` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 21 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 154 | START | 154 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 157 | START | 157 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `8` | `7` | 157 | START | 167 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `4` | `3` | 157 | START | 157 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `19` | `16` | 157 | START | 192 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `14` | `13` | 166 | END | 156 | 160 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 180 | START | 180 | 195 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 196 | START | 196 | 237 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 260 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 21–232
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 72 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 115 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 145 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 179 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 180 | 195 | 16 | inferred_complete_timeline |
| `Action_None` | 196 | 212 | 17 | inferred_complete_timeline |
| `Action_None` | 214 | 232 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 237 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 225 | 72 | inferred_complete_timeline |
| `Action_None` | 228 | 300 | 73 | inferred_complete_timeline |
| `Action_None` | 311 | 382 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 198 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 215 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 226 | 260 | 35 | inferred_complete_timeline |
| `Action_None` | 261 | 381 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_None` | 154 | 182 | 29 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 153 | 76 | inferred_complete_timeline |
| `Action_BallSnap` | 154 | 166 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 212 | 260 | 49 | inferred_complete_timeline |
| `Action_None` | 261 | 350 | 90 | inferred_complete_timeline |
| `Action_None` | 356 | 389 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PullBlock` | 157 | 174 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 194 | 204 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 153 | 51 | inferred_complete_timeline |
| `Action_None` | 154 | 320 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 114 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 153 | 25 | inferred_complete_timeline |
| `Action_None` | 154 | 192 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 153 | 74 | inferred_complete_timeline |
| `Action_None` | 154 | 234 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 153 | 142 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 210 | 338 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 153 | 144 | inferred_complete_timeline |
| `Action_None` | 154 | 205 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 132 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_None` | 154 | 174 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 153 | 45 | inferred_complete_timeline |
| `Action_None` | 154 | 175 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 49–185 | 133 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 58–384 | 324 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 192–348 | 151 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 197–286 | 66 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 216–389 | 119 | 7 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 243–357 | 82 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 245–342 | 92 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 257–277 | 21 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 257–298 | 42 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 267–292 | 26 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 284–334 | 51 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 287–389 | 83 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 294–340 | 36 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 299–342 | 44 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 299–314 | 16 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 306–389 | 82 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 316–389 | 67 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 320–378 | 59 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 325–352 | 28 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 359–372 | 9 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 367–371 | 5 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (LT) duration 104 frames exceeds threshold 90 frames [start=157, end=260].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (C) duration 104 frames exceeds threshold 90 frames [start=157, end=260].
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [154–166], lower_priority='Action_DownBlock' annotated_start=157, effective_Action_DownBlock_start=167.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [157-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [178-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [194-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-300] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-382] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-381] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-187] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [203-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [212-260] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-174] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-153] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-338] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [156-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-282] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-384] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [192-233] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-348] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-268] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-365] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-308] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-342] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-292] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-334] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-339] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-340] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-342] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-314] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-368] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-383] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-378] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-352] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-365] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-371] for track '35' has 1 frames without a visible bounding box.
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

</details>