# Play-Annotation-Generator Annotation Review — Counter_230

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_230`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 149 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 149 | START | 149 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `15` | `14` | 150 | START | 150 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 150 | START | 182 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `4` | `3` | 150 | START | 150 | 222 |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | `13` | `12` | 150 | START | 150 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `9` | 150 | START | 150 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `12` | `11` | 150 | START | 150 | 154 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 160 | END | 149 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `2` | `1` | 175 | START | 175 | 186 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `13` | `12` | 193 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 264 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_SnapReceive` | 149 | 160 | 12 | inferred_complete_timeline |
| `Action_None` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 175 | 186 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 320 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 150 | 154 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 157 | 162 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 215 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PullBlock` | 150 | 175 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 178 | 190 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 202 | 247 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 255 | 264 | 10 | inferred_complete_timeline |
| `Action_None` | 265 | 370 | 106 | inferred_complete_timeline |
| `Action_None` | 376 | 389 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_BallSnap` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 256 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 222 | 73 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 246 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 250 | 252 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 320 | 54 | inferred_complete_timeline |
| `Action_None` | 323 | 389 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 237 | 88 | inferred_complete_timeline |
| `Action_DownBlock` | 239 | 261 | 23 | inferred_complete_timeline |
| `Action_None` | 266 | 301 | 36 | inferred_complete_timeline |
| `Action_None` | 303 | 314 | 12 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 389 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 225 | 77 | inferred_complete_timeline |
| `Action_None` | 227 | 315 | 89 | inferred_complete_timeline |
| `Action_None` | 322 | 365 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 204 | 56 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 228 | 17 | inferred_complete_timeline |
| `Action_None` | 230 | 314 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–368
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 172 | 24 | inferred_complete_timeline |
| `Action_None` | 177 | 368 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–373
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 199 | 51 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 221 | 13 | inferred_complete_timeline |
| `Action_None` | 224 | 373 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 389 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 212 | 64 | inferred_complete_timeline |
| `Action_None` | 215 | 249 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 380 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_None` | 149 | 149 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–178 | 179 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 150–155 | 6 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 154–389 | 235 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 166–339 | 171 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 182–389 | 180 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 187–389 | 203 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 216–389 | 168 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 216–219 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 229–389 | 161 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 236–385 | 146 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 238–243 | 6 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 255–389 | 128 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 257–389 | 133 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 258–389 | 131 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 272–275 | 4 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 288–389 | 102 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 323–389 | 67 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `2` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 462: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 115 frames exceeds threshold 90 frames [start=150, end=264].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (LG) duration 115 frames exceeds threshold 90 frames [start=150, end=264].
- ⚠️ Segment 'Action_BallCarry' for track '12' has invalid range: start=193, end=178. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (RT) duration 115 frames exceeds threshold 90 frames [start=150, end=264].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 107 frames exceeds threshold 90 frames [start=150, end=256].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [149–160], lower_priority='Action_DownBlock' annotated_start=150, effective_Action_DownBlock_start=161.
- ⚠️ Action 'Action_None' range [149-212] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-249] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [175-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [250-252] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-320] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '4' starts at frame 149, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [149-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-315] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-365] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-199] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-373] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-368] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [150-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [178-190] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [202-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-370] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-380] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [150-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [157-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [150-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-215] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [239-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-301] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-314] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [149-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-186] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-256] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-267] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-339] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-312] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-389] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-372] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-351] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-371] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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