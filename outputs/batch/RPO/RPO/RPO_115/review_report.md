# Play-Annotation-Generator Annotation Review — RPO_115

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `RPO_115`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 213
- **Validation Warnings:** 276
- **Validation Errors:** 1
- **Overall Status:** FAILED
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `1` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 170
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `9` | `9` | 82 | START | 82 | 107 |
| ✅ EXACT | `Action_PullBall` | QB | `9` | `9` | 113 | START | 113 | 119 |
| ✅ EXACT | `Action_ThrowPass` | QB | `9` | `9` | 155 | START | 155 | 164 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ReadDefender` | 82 | 107 | 26 | inferred_complete_timeline |
| `Action_ReadDefender` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_PullBall` | 113 | 119 | 7 | inferred_complete_timeline |
| `Action_None` | 120 | 154 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 172 | 8 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_None` | 214 | 273 | 60 | inferred_complete_timeline |
| `Action_None` | 276 | 288 | 13 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 219 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 251 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 287 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 301 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 312 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 330 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 360 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 380 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 419 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 138 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 326 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 336 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 356 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 387 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 146 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 172 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 226 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 244 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 258 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 139 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 333 | 334 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 251 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 278 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 419 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 212 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 241 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 290 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 302 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 313 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 310 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 323 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 333 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 224 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 419 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 288 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 301 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–419 | 326 | 27 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 2–77 | 76 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 8–419 | 303 | 14 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 65–314 | 188 | 10 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 66–169 | 87 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 91–99 | 9 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 117–170 | 48 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 155–313 | 122 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 174–292 | 94 | 8 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 196–229 | 23 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 205–273 | 66 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 207–403 | 188 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 224–324 | 89 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 229–419 | 189 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 257–302 | 39 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 298–300 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 301–305 | 5 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 311–318 | 8 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 313–419 | 107 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 321–382 | 10 | 3 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 322–404 | 80 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 326–327 | 2 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 328–419 | 73 | 5 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 332–385 | 53 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 333–334 | 2 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 335–344 | 8 | 2 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 337–410 | 74 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 341–419 | 66 | 5 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 349–392 | 39 | 3 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 367–377 | 9 | 2 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 372–375 | 4 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 379–419 | 39 | 2 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 385–419 | 35 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 391–419 | 20 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['C', 'LG', 'RG', 'RT'].

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 203 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-288] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-219] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-251] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-287] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-301] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-312] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-330] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-360] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-380] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-419] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-310] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-323] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-333] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-212] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-290] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-313] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-419] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-419] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [82-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-288] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-278] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-333] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-145] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-326] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-336] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-356] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-387] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-146] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-172] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-226] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-244] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-188] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-212] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-275] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-296] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-356] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-366] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-372] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-376] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-391] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-398] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-408] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-414] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-19] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-270] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-290] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-317] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-170] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-244] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-303] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-188] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-211] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-270] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-219] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-219] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-315] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-393] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-403] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-300] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-312] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-324] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-326] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-290] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-302] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-300] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-305] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-318] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-419] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-323] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-360] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-382] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-368] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-404] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-365] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-387] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-405] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-419] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-361] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-385] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-344] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-410] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-350] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-356] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-375] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-387] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-419] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-356] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-380] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-392] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-377] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-387] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-419] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-419] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-394] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-404] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-415] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.

</details>