# Play-Annotation-Generator Annotation Review — Counter_214

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_214`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 42
- **Ball Tracks:** 1
- **Action Segments:** 130
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `11` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 97 | START | 97 | 99 |
| ✅ EXACT | `Action_DownBlock` | LG | `10` | `9` | 99 | START | 99 | 237 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `12` | `11` | 99 | START | 100 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 99 | START | 99 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `13` | `12` | 99 | START | 99 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `11` | `10` | 99 | START | 99 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 99 | END | 97 | 99 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 128 | START | 128 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 138 | START | 138 | 147 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 237 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 96 | 65 | inferred_complete_timeline |
| `Action_SnapReceive` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_None` | 100 | 127 | 28 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 138 | 197 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 147 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 389 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 99 | 169 | 71 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 179 | 236 | 58 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 242 | 389 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 147 | 51 | inferred_complete_timeline |
| `Action_None` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 181 | 83 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 230 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 238 | 389 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 237 | 139 | inferred_complete_timeline |
| `Action_None` | 238 | 389 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_BallSnap` | 97 | 99 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 237 | 138 | inferred_complete_timeline |
| `Action_None` | 238 | 389 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PullBlock` | 99 | 122 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 128 | 155 | 28 | inferred_complete_timeline |
| `Action_PullBlock` | 159 | 237 | 79 | inferred_complete_timeline |
| `Action_None` | 238 | 355 | 118 | inferred_complete_timeline |
| `Action_None` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 124 | 28 | inferred_complete_timeline |
| `Action_None` | 136 | 169 | 34 | inferred_complete_timeline |
| `Action_None` | 172 | 389 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 143 | 47 | inferred_complete_timeline |
| `Action_None` | 146 | 221 | 76 | inferred_complete_timeline |
| `Action_None` | 225 | 374 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 147 | 51 | inferred_complete_timeline |
| `Action_None` | 160 | 226 | 67 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 140 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 211 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 233 | 137 | inferred_complete_timeline |
| `Action_None` | 259 | 261 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 283 | 10 | inferred_complete_timeline |
| `Action_None` | 289 | 389 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 122 | 26 | inferred_complete_timeline |
| `Action_None` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_None` | 97 | 200 | 104 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 270 | 16 | inferred_complete_timeline |
| `Action_None` | 272 | 389 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–389 | 385 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 74–136 | 63 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 123–289 | 139 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 160–290 | 119 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 163–389 | 227 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 166–388 | 221 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–389 | 167 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 193–220 | 19 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 193–389 | 196 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 200–389 | 190 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 212–389 | 167 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 221–389 | 169 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 237–342 | 97 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 243–389 | 147 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 255–389 | 135 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 282–283 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 307–317 | 9 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 312–389 | 78 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 314–359 | 22 | 4 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 327–383 | 35 | 6 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 334–344 | 7 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 344–345 | 2 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 350–389 | 38 | 3 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 378–383 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 27 | 74 | 40 | 83.3% | 28–35 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `12` (C): Annotated start 99 != Inferred start 100
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '9' (LG) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [97–99], lower_priority='Action_DownBlock' annotated_start=99, effective_Action_DownBlock_start=100.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '12' (RG) duration 139 frames exceeds threshold 90 frames [start=99, end=237].
- ⚠️ Action 'Action_None' range [97-233] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-147] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-374] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-181] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [99-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [172-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [175-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [179-236] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [99-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [128-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-140] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-211] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-270] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-136] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-274] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-262] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-283] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-349] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-388] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-389] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-380] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-240] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-342] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-332] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-332] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-349] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-377] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-389] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-383] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>