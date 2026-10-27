# Play-Annotation-Generator Annotation Review — Counter_213

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_213`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 96
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `3` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 96 | START | 96 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 98 | START | 98 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 98 | START | 98 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `22` | `21` | 98 | START | 98 | 125 |
| ✅ EXACT | `Action_PullBlock` | RG | `19` | `18` | 98 | START | 98 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `3` | `2` | 98 | START | 98 | 186 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 98 | END | 96 | 98 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 125 | START | 125 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 136 | START | 136 | 348 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 124 | 26 | inferred_complete_timeline |
| `Action_Handoff` | 125 | 135 | 11 | inferred_complete_timeline |
| `Action_None` | 136 | 327 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 348 | 213 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 98 | 186 | 89 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 359 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 359 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 125 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 118 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 210 | 87 | inferred_complete_timeline |
| `Action_DownBlock` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BallSnap` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_None` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_None` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_None` | 154 | 191 | 38 | inferred_complete_timeline |
| `Action_None` | 196 | 359 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PullBlock` | 98 | 235 | 138 | inferred_complete_timeline |
| `Action_None` | 236 | 359 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 359 | 264 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 155 | 60 | inferred_complete_timeline |
| `Action_None` | 158 | 348 | 191 | inferred_complete_timeline |
| `Action_None` | 350 | 358 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 307 | 212 | inferred_complete_timeline |
| `Action_None` | 310 | 314 | 5 | inferred_complete_timeline |
| `Action_None` | 319 | 321 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 359 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 218 | 123 | inferred_complete_timeline |
| `Action_None` | 237 | 359 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 143 | 48 | inferred_complete_timeline |
| `Action_None` | 145 | 154 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 217 | 122 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 165 | 70 | inferred_complete_timeline |
| `Action_None` | 176 | 359 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 359 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 229 | 134 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 174 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–126 | 127 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–359 | 346 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 149–359 | 207 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 154–359 | 204 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 180–239 | 41 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 186–359 | 174 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 219–359 | 60 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 248–359 | 112 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 248–359 | 112 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 254–359 | 79 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 256–323 | 68 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 265–270 | 5 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 280–305 | 12 | 3 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 350–357 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 428: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (Unknown) duration 138 frames exceeds threshold 90 frames [start=98, end=235].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '18' (RG) duration 138 frames exceeds threshold 90 frames [start=98, end=235].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (LG) duration 118 frames exceeds threshold 90 frames [start=98, end=215].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
- ⚠️ Action 'Action_None' range [96-307] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [98-186] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [203-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-348] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-143] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-217] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-348] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-191] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-327] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [124-210] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [214-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-323] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>