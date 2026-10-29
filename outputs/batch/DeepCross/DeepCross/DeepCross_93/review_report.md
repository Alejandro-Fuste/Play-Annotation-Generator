# Play-Annotation-Generator Annotation Review — DeepCross_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_93`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `16` | `16` | 19 | START | 19 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `11` | `11` | 22 | START | 22 | 171 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `15` | `15` | 22 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 22 | START | 22 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 22 | START | 22 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 22 | START | 22 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `1` | `1` | 32 | START | 32 | 97 |
| ✅ EXACT | `Action_SnapReceive` | C | `15` | `15` | 32 | END | 19 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | C | `15` | `15` | 131 | START | 131 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `1` | `1` | 203 | START | 203 | 234 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 243 | 225 | inferred_complete_timeline |
| `Action_None` | 285 | 292 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 32 | 97 | 66 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 100 | 195 | 96 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 234 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 243 | 248 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–326
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 91 | 73 | inferred_complete_timeline |
| `Action_None` | 95 | 292 | 198 | inferred_complete_timeline |
| `Action_None` | 295 | 322 | 28 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 329 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 171 | 150 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 48 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 72 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 171 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 33 | 130 | 98 | inferred_complete_timeline |
| `Action_ThrowPass` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 170 | 29 | inferred_complete_timeline |
| `Action_None` | 185 | 248 | 64 | inferred_complete_timeline |
| `Action_None` | 252 | 269 | 18 | inferred_complete_timeline |
| `Action_None` | 271 | 317 | 47 | inferred_complete_timeline |
| `Action_None` | 319 | 323 | 5 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 63 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 170 | 104 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 268 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 270 | 297 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 302 | 329 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 134 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 170 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 228 | 210 | inferred_complete_timeline |
| `Action_None` | 232 | 243 | 12 | inferred_complete_timeline |
| `Action_None` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_None` | 261 | 329 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 114 | 96 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_None` | 136 | 158 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 329 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 103 | 85 | inferred_complete_timeline |
| `Action_None` | 112 | 257 | 146 | inferred_complete_timeline |
| `Action_None` | 259 | 268 | 10 | inferred_complete_timeline |
| `Action_None` | 280 | 291 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 32 | 14 | inferred_complete_timeline |
| `Action_None` | 33 | 44 | 12 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 189 | 171 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 83 | 65 | inferred_complete_timeline |
| `Action_None` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_None` | 102 | 132 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 267 | 249 | inferred_complete_timeline |
| `Action_None` | 277 | 288 | 12 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 305 | 309 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–185 | 184 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–309 | 298 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–313 | 314 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 9–329 | 267 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 9–30 | 22 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 64–84 | 10 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 83–165 | 80 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 147–171 | 25 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 173–176 | 4 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 185–223 | 39 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 185–329 | 138 | 4 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 187–252 | 64 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 192–197 | 6 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 194–329 | 136 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 213–329 | 63 | 11 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 214–329 | 110 | 4 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 220–222 | 3 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 220–328 | 80 | 7 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 244–248 | 5 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 247–329 | 69 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 255–329 | 63 | 4 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 265–267 | 3 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `15` (C)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 95: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 96: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 96: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '15' has invalid range: start=22, end=18. Clamping end to start.
- ⚠️ Action 'Action_None' range [19-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-322] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [32-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-234] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-241] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [243-248] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-83] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-158] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-228] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-268] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-291] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-99] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-292] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-309] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-189] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [131-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-170] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-248] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-317] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-171] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-313] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [189-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [270-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [302-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-30] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-171] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-223] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-252] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-329] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-270] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-291] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-316] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-292] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-248] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-286] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-317] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-328] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-274] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>