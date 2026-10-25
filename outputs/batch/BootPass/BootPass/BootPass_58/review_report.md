# Play-Annotation-Generator Annotation Review — BootPass_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_58`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 2
- **Action Segments:** 107
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `17` | N/A |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `23` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 54 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `17` | N/A | 115 | START | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 137 | START | 137 | 153 |
| ✅ EXACT | `Action_RunBlock` | RT | `0` | `0` | 146 | START | 146 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 146 | START | 154 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `2` | `2` | 146 | START | 146 | 207 |
| ✅ EXACT | `Action_RunBlock` | LG | `8` | `8` | 146 | START | 146 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `9` | `9` | 146 | START | 146 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 153 | END | 137 | 153 |
| ✅ EXACT | `Action_SecureCatch` | RT | `0` | `0` | 154 | START | 154 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `23` | `21` | 163 | START | 164 | 167 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `23` | `21` | 177 | START | 177 | 179 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `23` | `21` | 180 | START | 180 | 226 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_SnapReceive` | 137 | 153 | 17 | inferred_complete_timeline |
| `Action_None` | 154 | 167 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 16 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 38 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 136 | 95 | inferred_complete_timeline |
| `Action_None` | 137 | 256 | 120 | inferred_complete_timeline |
| `Action_None` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_None` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 207 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 214 | 271 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 145 | 92 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 152 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_BallSnap` | 137 | 153 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 154 | 174 | 21 | inferred_complete_timeline |
| `Action_RunBlock` | 187 | 246 | 60 | inferred_complete_timeline |
| `Action_RunBlock` | 251 | 278 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 180 | 268 | 89 | inferred_complete_timeline |
| `Action_RunBlock` | 270 | 280 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_SecureCatch` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 173 | 12 | inferred_complete_timeline |
| `Action_None` | 178 | 192 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 165 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 219 | 83 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 271 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 136 | 90 | inferred_complete_timeline |
| `Action_None` | 137 | 187 | 51 | inferred_complete_timeline |
| `Action_None` | 192 | 260 | 69 | inferred_complete_timeline |
| `Action_None` | 262 | 329 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 223 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 161 | 25 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 265 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_None` | 137 | 277 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 40–206 | 167 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 64–272 | 197 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 142–262 | 93 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 150–277 | 80 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 158–222 | 65 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 164–274 | 110 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 186–271 | 74 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 189–193 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 195–199 | 5 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 195–298 | 104 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 205–271 | 67 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 210–219 | 10 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 247–258 | 12 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 252–274 | 23 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 263–324 | 62 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 268–290 | 8 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 269–307 | 39 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 269–300 | 32 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 271–275 | 5 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 276–278 | 3 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 279–329 | 51 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 279–282 | 4 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 280–329 | 50 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 283–329 | 41 | 2 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 314–329 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 50 | 57 | 8 | 100.0% | None |
| `17` | `17` | 109 | 133 | 6 | 24.0% | 113–114, 116–132 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ThrowPass` on target `17` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 96: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [137–153], lower_priority='Action_RunBlock' annotated_start=146, effective_Action_RunBlock_start=154.
- ⚠️ Action 'Action_None' range [162-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-192] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [146-207] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [214-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-223] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-271] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [146-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [146-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [180-268] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [270-280] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [154-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [187-246] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [251-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-166] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-272] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-277] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [164-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-274] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-307] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-321] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>