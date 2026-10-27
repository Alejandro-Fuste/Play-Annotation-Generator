# Play-Annotation-Generator Annotation Review — Counter_219

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_219`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | CB1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 8 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 63 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `9` | `Group` | 0 | START | 0 | 162 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 163 | START | 163 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 166 | START | 175 | 177 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | `21` | `20` | 166 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | CB1 | `11` | `10` | 166 | START | 166 | 248 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `12` | `11` | 166 | START | 166 | 179 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 174 | END | 163 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 207 | START | 207 | 243 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 248 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_SnapReceive` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_None` | 175 | 206 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 243 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 253 | 359 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 196 | 34 | inferred_complete_timeline |
| `Action_None` | 203 | 214 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 305 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 166 | 179 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 182 | 187 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–250
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 26 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 162 | 127 | inferred_complete_timeline |
| `Action_BallSnap` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 63–152
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 63 | 76 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 105 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 152 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 106 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 139 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 155 | 14 | inferred_complete_timeline |
| `Action_None` | 237 | 250 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 106 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 158 | 27 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 232 | 13 | inferred_complete_timeline |
| `Action_None` | 279 | 359 | 81 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 209 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PullBlock` | 166 | 248 | 83 | inferred_complete_timeline |
| `Action_None` | 249 | 359 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 359 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 204 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 238 | 76 | inferred_complete_timeline |
| `Action_None` | 240 | 316 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_None` | 163 | 332 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–259 | 119 | 11 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–109 | 66 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 3–83 | 28 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 183–359 | 173 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 220–359 | 138 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 225–228 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 244–322 | 9 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 252–359 | 108 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 264–359 | 87 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 272–359 | 84 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 283–359 | 64 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 298–359 | 62 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 303–359 | 57 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 303–359 | 57 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 307–359 | 53 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 308–349 | 42 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 326–349 | 5 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 339–359 | 21 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `21` (RG)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [163–174], lower_priority='Action_DownBlock' annotated_start=166, effective_Action_DownBlock_start=175.
- ⚠️ Segment 'Action_DownBlock' for track '20' has invalid range: start=166, end=152. Clamping end to start.
- ⚠️ Action 'Action_None' range [163-332] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-214] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-316] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [166-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [182-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-61] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-137] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-229] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-106] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-125] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-155] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-250] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-158] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-232] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-359] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [163-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [247-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-105] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-349] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>