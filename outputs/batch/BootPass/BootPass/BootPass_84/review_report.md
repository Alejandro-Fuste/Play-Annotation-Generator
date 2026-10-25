# Play-Annotation-Generator Annotation Review — BootPass_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_84`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 135
- **Validation Warnings:** 149
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `34` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `0` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `1` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `10` | `10` | 86 | START | 86 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `10` | `10` | 93 | START | 104 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `2` | `2` | 93 | START | 93 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `6` | `6` | 93 | START | 93 | 238 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `7` | `7` | 93 | START | 93 | 154 |
| ✅ EXACT | `Action_RunBlock` | LG | `9` | `9` | 93 | START | 93 | 204 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 103 | END | 86 | 103 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `3` | `3` | 108 | START | 108 | 140 |
| ✅ EXACT | `Action_BootAway` | QB | `3` | `3` | 141 | START | 141 | 173 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `15` | `15` | 141 | START | 141 | 142 |
| ✅ EXACT | `Action_ThrowPass` | QB | `3` | `3` | 177 | START | 177 | 187 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `34` | `31` | 226 | START | 226 | 241 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 86 | 103 | 18 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_FakeHandoff` | 108 | 140 | 33 | inferred_complete_timeline |
| `Action_BootAway` | 141 | 173 | 33 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_ThrowPass` | 177 | 187 | 11 | inferred_complete_timeline |
| `Action_None` | 188 | 329 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 120 | 35 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 241 | 104 | inferred_complete_timeline |
| `Action_None` | 245 | 278 | 34 | inferred_complete_timeline |
| `Action_None` | 280 | 285 | 6 | inferred_complete_timeline |
| `Action_None` | 289 | 329 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 119 | 34 | inferred_complete_timeline |
| `Action_None` | 150 | 307 | 158 | inferred_complete_timeline |
| `Action_None` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 167 | 75 | inferred_complete_timeline |
| `Action_RunBlock` | 169 | 221 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 227 | 281 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 204 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 104 | 153 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 224 | 329 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 154 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 160 | 174 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 208 | 225 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 228 | 329 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 238 | 146 | inferred_complete_timeline |
| `Action_RunBlock` | 241 | 329 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 135 | 50 | inferred_complete_timeline |
| `Action_None` | 140 | 181 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 219 | 134 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_None` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_None` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_None` | 194 | 207 | 14 | inferred_complete_timeline |
| `Action_None` | 214 | 265 | 52 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 329 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 85 | 53 | inferred_complete_timeline |
| `Action_None` | 86 | 187 | 102 | inferred_complete_timeline |
| `Action_None` | 192 | 223 | 32 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_None` | 242 | 249 | 8 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 262 | 8 | inferred_complete_timeline |
| `Action_None` | 272 | 329 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 2–140 | 129 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 4–146 | 131 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 9–146 | 20 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 126–166 | 41 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 132–139 | 4 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 134–329 | 193 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 148–329 | 180 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 169–196 | 6 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 180–241 | 58 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 183–329 | 136 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 189–329 | 141 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 191–285 | 11 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 200–329 | 126 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 202–329 | 128 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 202–322 | 118 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 205–329 | 120 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 209–328 | 113 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 210–328 | 112 | 4 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 223–249 | 27 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 227–329 | 101 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 258–329 | 66 | 3 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 263–329 | 55 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 272–317 | 11 | 3 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 306–329 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [86–103], lower_priority='Action_RunBlock' annotated_start=93, effective_Action_RunBlock_start=104.
- ⚠️ Action 'Action_None' range [86-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-307] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-278] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [169-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [227-281] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [160-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [191-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [194-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [204-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [208-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-187] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [86-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [104-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-265] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-296] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-298] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-296] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-321] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-300] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-307] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-306] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-288] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>