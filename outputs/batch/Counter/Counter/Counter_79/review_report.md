# Play-Annotation-Generator Annotation Review — Counter_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_79`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 5 | START | 5 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 5 | START | 5 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 5 | START | 5 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 5 | START | 5 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 5 | START | 5 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 82 | START | 82 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `22` | `21` | 86 | START | 96 | 147 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `17` | 86 | START | 86 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 86 | START | 86 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 95 | END | 82 | 95 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 100 | START | 100 | 124 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `19` | `18` | 125 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 166 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 95 | 14 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 124 | 25 | inferred_complete_timeline |
| `Action_None` | 125 | 149 | 25 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_None` | 176 | 359 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 115 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 190 | 109 | inferred_complete_timeline |
| `Action_None` | 205 | 359 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 85 | 81 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 86 | 147 | 62 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 149 | 166 | 18 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 336 | 255 | inferred_complete_timeline |
| `Action_None` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–147
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 85 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 86 | 147 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 95 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 147 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 359 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |
| `Action_None` | 215 | 359 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–182
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 182 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 118 | 37 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 359 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 125 | 44 | inferred_complete_timeline |
| `Action_None` | 133 | 160 | 28 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–176
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 107 | 26 | inferred_complete_timeline |
| `Action_None` | 120 | 176 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 136 | 55 | inferred_complete_timeline |
| `Action_None` | 145 | 359 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–358
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 358 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–324
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 279 | 198 | inferred_complete_timeline |
| `Action_None` | 283 | 324 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 359 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 189 | 108 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 232 | 36 | inferred_complete_timeline |
| `Action_None` | 237 | 359 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 81 | 77 | inferred_complete_timeline |
| `Action_None` | 82 | 276 | 195 | inferred_complete_timeline |
| `Action_None` | 278 | 327 | 50 | inferred_complete_timeline |
| `Action_None` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 122–359 | 233 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 175–359 | 182 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 181–359 | 174 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 197–359 | 163 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 253–261 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 258–260 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `19` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '18' has invalid range: start=125, end=115. Clamping end to start.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [82–95], lower_priority='Action_DownBlock' annotated_start=86, effective_Action_DownBlock_start=96.
- ⚠️ Action 'Action_None' range [82-118] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-276] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [86-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-232] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-279] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-324] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-176] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-149] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-358] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [86-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-336] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-155] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-233] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '29' has 1 frames without a visible bounding box.
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