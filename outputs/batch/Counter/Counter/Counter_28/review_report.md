# Play-Annotation-Generator Annotation Review — Counter_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_28`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 1
- **Action Segments:** 92
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 119 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 120 | START | 120 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `10` | 127 | START | 127 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 127 | START | 136 | 137 |
| ✅ EXACT | `Action_PullBlock` | RG | `10` | `9` | 127 | START | 127 | 147 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `4` | `3` | 127 | START | 127 | 207 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 135 | END | 120 | 135 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 162 | START | 162 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `0` | 179 | START | 179 | 191 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 207 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_SnapReceive` | 120 | 135 | 16 | inferred_complete_timeline |
| `Action_None` | 136 | 161 | 26 | inferred_complete_timeline |
| `Action_Handoff` | 162 | 178 | 17 | inferred_complete_timeline |
| `Action_None` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 201 | 287 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 127 | 207 | 81 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 168 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 144 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 147 | 207 | 61 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_BallSnap` | 120 | 135 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 151 | 194 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 207 | 12 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PullBlock` | 127 | 147 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 299 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 171 | 52 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 157 | 38 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 171 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 166 | 19 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 141 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 171 | 52 | inferred_complete_timeline |
| `Action_None` | 173 | 198 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 203 | 84 | inferred_complete_timeline |
| `Action_None` | 205 | 208 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_None` | 120 | 165 | 46 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 9–192 | 184 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 118–122 | 5 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 123–177 | 49 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 146–299 | 151 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 146–256 | 111 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 167–205 | 37 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 170–179 | 10 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 173–255 | 75 | 5 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 185–186 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 187–299 | 113 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 199–299 | 101 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 219–299 | 80 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 220–299 | 77 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 250–299 | 50 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 255–272 | 18 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 274–299 | 26 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 283–299 | 17 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 290–299 | 8 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 292–293 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `31` | 179 | 206 | 4 | 14.3% | 181–200, 202–205 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [120–135], lower_priority='Action_DownBlock' annotated_start=127, effective_Action_DownBlock_start=136.
- ⚠️ Action 'Action_BallCarry' range [179-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 208, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [208-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-299] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-198] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [127-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-141] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [151-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-166] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-192] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-285] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-276] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-286] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>