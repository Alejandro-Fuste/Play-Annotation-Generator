# Play-Annotation-Generator Annotation Review — Counter_373

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_373`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 4 | START | 4 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 4 | START | 4 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `11` | `Group` | 4 | START | 4 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 4 | START | 4 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 4 | START | 4 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 4 | START | 4 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 4 | START | 4 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 4 | START | 4 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 4 | START | 4 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 4 | START | 4 | 107 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | QB | `18` | `17` | 108 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LG | `21` | `20` | 111 | START | 111 | 199 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `6` | `5` | 111 | START | 111 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 111 | START | 111 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB2 | `3` | `2` | 111 | START | 111 | 166 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 114 | END | 108 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 143 | START | 143 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `11` | `10` | 158 | START | 158 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 201 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 108 | 114 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 142 | 28 | inferred_complete_timeline |
| `Action_Handoff` | 143 | 157 | 15 | inferred_complete_timeline |
| `Action_None` | 158 | 329 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–265
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 157 | 154 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 180 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 201 | 265 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 110 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 111 | 166 | 56 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 212 | 105 | inferred_complete_timeline |
| `Action_None` | 220 | 311 | 92 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–310
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 303 | 196 | inferred_complete_timeline |
| `Action_None` | 306 | 310 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 139 | 32 | inferred_complete_timeline |
| `Action_None` | 142 | 329 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 329 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 110 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 199 | 89 | inferred_complete_timeline |
| `Action_None` | 202 | 270 | 69 | inferred_complete_timeline |
| `Action_None` | 274 | 284 | 11 | inferred_complete_timeline |
| `Action_None` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 110 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 111 | 157 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 162 | 201 | 40 | inferred_complete_timeline |
| `Action_None` | 202 | 214 | 13 | inferred_complete_timeline |
| `Action_None` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_None` | 237 | 286 | 50 | inferred_complete_timeline |
| `Action_None` | 302 | 329 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 329 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–177
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 132 | 25 | inferred_complete_timeline |
| `Action_None` | 134 | 177 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 304 | 197 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 329 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–316
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 164 | 57 | inferred_complete_timeline |
| `Action_None` | 167 | 177 | 11 | inferred_complete_timeline |
| `Action_None` | 186 | 237 | 52 | inferred_complete_timeline |
| `Action_None` | 241 | 316 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–205
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 205 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–296
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 176 | 69 | inferred_complete_timeline |
| `Action_None` | 215 | 225 | 11 | inferred_complete_timeline |
| `Action_None` | 227 | 292 | 66 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–220
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 139 | 32 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 220 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 329 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–194
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 184 | 77 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 329 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–225
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 204 | 97 | inferred_complete_timeline |
| `Action_None` | 209 | 218 | 10 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–291
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_None` | 108 | 282 | 175 | inferred_complete_timeline |
| `Action_None` | 285 | 291 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 4–133 | 130 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 155–329 | 151 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 186–227 | 36 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 228–329 | 97 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 230–329 | 92 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 235–296 | 60 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 241–258 | 17 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 242–329 | 88 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 258–270 | 13 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 274–329 | 48 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 276–329 | 54 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 322–329 | 8 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `18` (QB)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 748: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (LG) duration 91 frames exceeds threshold 90 frames [start=111, end=201].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 91 frames exceeds threshold 90 frames [start=111, end=201].
- ⚠️ Action 'Action_None' range [108-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-311] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [111-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [171-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-205] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-303] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-292] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [158-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [201-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-177] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-282] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-304] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-315] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-139] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-237] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-316] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-270] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [111-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-286] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-194] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-303] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>