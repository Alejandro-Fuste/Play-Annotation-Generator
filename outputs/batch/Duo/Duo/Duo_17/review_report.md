# Play-Annotation-Generator Annotation Review — Duo_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_17`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_ComboBlock` | LB3 | defense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | LB3 | defense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 285 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 323 |
| ⚠️ START CHANGED | `Action_ComboBlock` | LB3 | `15` | `15` | 201 | START | 204 | 220 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | `17` | `17` | 201 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 218 | START | 218 | 249 |
| ✅ EXACT | `Action_BlockSecondLevel` | LB3 | `15` | `15` | 221 | START | 221 | 253 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 253 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 287 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_BallCarry` | 218 | 249 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 328 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 191 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 241 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 323 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 285 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 239 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 259 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 273 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 305 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 328 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 136 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 208 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 221 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 328 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 238 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 304 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 320 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 323 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 219 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 248 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 260 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 263 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 283 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 319 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 322 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 292 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |
| `Action_ComboBlock` | 204 | 220 | 17 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 221 | 253 | 33 | inferred_complete_timeline |
| `Action_None` | 254 | 311 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–292 | 263 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 257–328 | 57 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 265–328 | 64 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 265–328 | 63 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 267–315 | 34 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 282–328 | 47 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 285–328 | 39 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 293–323 | 29 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 298–303 | 6 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 299–328 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ComboBlock` for actor_track_id `15` (LB3): Annotated start 201 != Inferred start 204
- ❌ Missing segment for action `Action_ComboBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 35: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '17' has invalid range: start=201, end=186. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-262] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-249] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [263-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-304] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-248] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-206] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-285] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-311] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-259] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-305] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-136] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-292] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-128] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-287] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-271] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-328] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-277] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-297] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-310] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-301] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-303] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>