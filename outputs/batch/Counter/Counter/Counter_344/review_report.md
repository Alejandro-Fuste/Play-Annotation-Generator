# Play-Annotation-Generator Annotation Review — Counter_344

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_344`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE2 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DT1 | defense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 126 |
| ✅ EXACT | `Action_BallSnap` | QB | `14` | `13` | 127 | START | 127 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE2 | `1` | `0` | 130 | START | 130 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `14` | 130 | START | 137 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `2` | `1` | 130 | START | 130 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `4` | `3` | 130 | START | 130 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `3` | `2` | 130 | START | 130 | 191 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `7` | `6` | 139 | END | 127 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DT1 | `7` | `6` | 158 | START | 158 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT1 | `7` | `6` | 175 | START | 175 | 206 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 220 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_BallSnap` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 140 | 281 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 220 | 91 | inferred_complete_timeline |
| `Action_None` | 221 | 233 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 161 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 156 | 27 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 181 | 217 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 220 | 1 | inferred_complete_timeline |
| `Action_None` | 221 | 221 | 1 | inferred_complete_timeline |
| `Action_None` | 233 | 268 | 36 | inferred_complete_timeline |
| `Action_None` | 271 | 352 | 82 | inferred_complete_timeline |
| `Action_None` | 356 | 359 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 185 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 220 | 33 | inferred_complete_timeline |
| `Action_None` | 221 | 345 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 183 | 57 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 181 | 55 | inferred_complete_timeline |
| `Action_None` | 185 | 235 | 51 | inferred_complete_timeline |
| `Action_None` | 273 | 306 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_SnapReceive` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 140 | 157 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 158 | 170 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 174 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 206 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 359 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |
| `Action_None` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 190 | 64 | inferred_complete_timeline |
| `Action_None` | 193 | 341 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 157 | 31 | inferred_complete_timeline |
| `Action_None` | 162 | 192 | 31 | inferred_complete_timeline |
| `Action_None` | 195 | 218 | 24 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 227 | 236 | 10 | inferred_complete_timeline |
| `Action_None` | 238 | 352 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 214 | 88 | inferred_complete_timeline |
| `Action_None` | 218 | 223 | 6 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |
| `Action_None` | 243 | 265 | 23 | inferred_complete_timeline |
| `Action_None` | 268 | 359 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_None` | 127 | 241 | 115 | inferred_complete_timeline |
| `Action_None` | 251 | 276 | 26 | inferred_complete_timeline |
| `Action_None` | 283 | 300 | 18 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 359 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–304 | 291 | 7 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 137–308 | 162 | 5 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 147–156 | 5 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 159–259 | 64 | 6 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 171–356 | 180 | 4 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 176–359 | 180 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 184–219 | 34 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 192–232 | 41 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 193–200 | 8 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 196–335 | 140 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 198–339 | 141 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 198–359 | 154 | 4 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 217–287 | 67 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 233–359 | 126 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 234–356 | 112 | 6 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 248–359 | 112 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 249–359 | 111 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 258–292 | 35 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 305–359 | 53 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 689: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 690: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 690: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (TE2) duration 91 frames exceeds threshold 90 frames [start=130, end=220].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (RG) duration 91 frames exceeds threshold 90 frames [start=130, end=220].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '3' (LG) duration 91 frames exceeds threshold 90 frames [start=130, end=220].
- ⚠️ Action 'Action_None' range [221-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [130-191] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [193-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [198-205] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [181-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 221, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [221-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-352] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-183] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-341] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [158-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-276] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-300] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-161] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-235] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-306] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-192] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-236] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-214] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-281] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-324] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-352] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-215] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-335] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-339] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-283] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-290] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-322] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-335] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-356] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>