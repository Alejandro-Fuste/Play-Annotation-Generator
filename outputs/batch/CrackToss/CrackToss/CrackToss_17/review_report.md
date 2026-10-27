# Play-Annotation-Generator Annotation Review — CrackToss_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_17`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | WR3 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 170 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 171 | START | 171 | 185 |
| ✅ EXACT | `Action_CrackBlock` | WR3 | `1` | `0` | 174 | START | 174 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RT | `18` | `17` | 174 | START | 174 | 189 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 185 | END | 171 | 185 |
| ✅ EXACT | `Action_Toss` | QB | `19` | `18` | 194 | START | 194 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `15` | 207 | START | 207 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 256 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_SnapReceive` | 171 | 185 | 15 | inferred_complete_timeline |
| `Action_None` | 186 | 193 | 8 | inferred_complete_timeline |
| `Action_Toss` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_None` | 207 | 359 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 206 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 217 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 299 | 80 | inferred_complete_timeline |
| `Action_BallCarry` | 306 | 319 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 221 | 51 | inferred_complete_timeline |
| `Action_None` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 200 | 30 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_CrackBlock` | 174 | 189 | 16 | inferred_complete_timeline |
| `Action_None` | 260 | 331 | 72 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 337 | 338 | 2 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 189 | 19 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 189 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallSnap` | 171 | 185 | 15 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 189 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 214 | 256 | 43 | inferred_complete_timeline |
| `Action_None` | 257 | 316 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 209 | 5 | inferred_complete_timeline |
| `Action_None` | 248 | 359 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 189 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 253 | 6 | inferred_complete_timeline |
| `Action_None` | 257 | 359 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 189 | 19 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 218 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 283 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 359 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 213 | 43 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 225 | 359 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 277 | 107 | inferred_complete_timeline |
| `Action_None` | 283 | 291 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 359 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 253 | 83 | inferred_complete_timeline |
| `Action_None` | 256 | 300 | 45 | inferred_complete_timeline |
| `Action_None` | 302 | 308 | 7 | inferred_complete_timeline |
| `Action_None` | 317 | 322 | 6 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 359 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 288 | 118 | inferred_complete_timeline |
| `Action_None` | 291 | 297 | 7 | inferred_complete_timeline |
| `Action_None` | 311 | 359 | 49 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–188 | 189 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 206–359 | 134 | 8 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 214–359 | 122 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 221–256 | 36 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 246–269 | 24 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 247–359 | 112 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 251–359 | 101 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 251–359 | 106 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 251–359 | 86 | 5 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 251–359 | 109 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 263–280 | 18 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 300–327 | 28 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 311–359 | 49 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 318–354 | 25 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 36: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_CrackBlock' range [174-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-331] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-189] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-221] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-200] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-359] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-359] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-299] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [306-319] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-300] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [214-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-316] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-288] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-284] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-293] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-359] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-346] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-280] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-337] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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