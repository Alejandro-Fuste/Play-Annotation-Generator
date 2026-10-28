# Play-Annotation-Generator Annotation Review — Draw_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_29`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 32 | START | 32 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 32 | START | 32 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 32 | START | 32 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 32 | START | 32 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 32 | START | 32 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 32 | START | 32 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 32 | START | 32 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 32 | START | 32 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 32 | START | 32 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 32 | START | 32 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 32 | START | 32 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 75 | START | 75 | 87 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `9` | 78 | START | 78 | 181 |
| ✅ EXACT | `Action_PassBlock` | RT | `14` | `13` | 78 | START | 78 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `17` | 78 | START | 78 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `20` | 78 | START | 78 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `22` | `21` | 78 | START | 88 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 87 | END | 75 | 87 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `17` | `16` | 93 | START | 93 | 126 |
| ✅ EXACT | `Action_BallCarry` | QB | `17` | `16` | 127 | START | 127 | 144 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 181 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 32–144
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 144 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 206 | 132 | inferred_complete_timeline |
| `Action_None` | 209 | 329 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 32–152
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 148 | 74 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 329 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 32–310
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 310 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 177 | 103 | inferred_complete_timeline |
| `Action_None` | 182 | 284 | 103 | inferred_complete_timeline |
| `Action_None` | 292 | 297 | 6 | inferred_complete_timeline |
| `Action_None` | 300 | 312 | 13 | inferred_complete_timeline |
| `Action_None` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 181 | 104 | inferred_complete_timeline |
| `Action_None` | 182 | 257 | 76 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 181 | 34 | inferred_complete_timeline |
| `Action_None` | 195 | 262 | 68 | inferred_complete_timeline |
| `Action_None` | 265 | 273 | 9 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 32–322
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 108 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 181 | 72 | inferred_complete_timeline |
| `Action_None` | 182 | 235 | 54 | inferred_complete_timeline |
| `Action_None` | 242 | 283 | 42 | inferred_complete_timeline |
| `Action_None` | 305 | 311 | 7 | inferred_complete_timeline |
| `Action_None` | 314 | 322 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 126 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 181 | 50 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 32–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 77 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 181 | 104 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 32–117
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 117 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 258 | 184 | inferred_complete_timeline |
| `Action_None` | 260 | 329 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 32–100
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 100 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 329 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 329 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 32–282
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 192 | 118 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 224 | 26 | inferred_complete_timeline |
| `Action_None` | 229 | 257 | 29 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 144 | 70 | inferred_complete_timeline |
| `Action_None` | 148 | 153 | 6 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_None` | 179 | 309 | 131 | inferred_complete_timeline |
| `Action_None` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 293 | 219 | inferred_complete_timeline |
| `Action_None` | 295 | 303 | 9 | inferred_complete_timeline |
| `Action_None` | 306 | 312 | 7 | inferred_complete_timeline |
| `Action_None` | 316 | 324 | 9 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 283 | 209 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 295 | 7 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 32–182
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 182 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 32–329
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 74 | 43 | inferred_complete_timeline |
| `Action_None` | 75 | 230 | 156 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 124–329 | 177 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 169–329 | 148 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 173–329 | 145 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 180–329 | 150 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 187–254 | 65 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 264–279 | 14 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 296–308 | 13 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [75–87], lower_priority='Action_PassBlock' annotated_start=78, effective_Action_PassBlock_start=88.
- ⚠️ Action 'Action_None' range [75-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-284] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-312] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-310] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-224] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-257] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-309] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-257] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-100] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-293] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-303] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-262] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '21' starts at frame 88, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [88-98] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-283] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-322] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-263] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-196] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-329] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-246] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-272] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-308] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '33' has 1 frames without a visible bounding box.
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