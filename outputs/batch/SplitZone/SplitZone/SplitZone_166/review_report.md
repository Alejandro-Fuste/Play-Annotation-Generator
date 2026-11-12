# Play-Annotation-Generator Annotation Review — SplitZone_166

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_166`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 216
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 130
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `11` | `Group` | 6 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 6 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 6 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 6 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 6 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 6 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 6 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 6 | START | 0 | 176 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 174 | START | 174 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 177 | START | 177 | 237 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 177 | START | 177 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 177 | START | 177 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 177 | START | 193 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 177 | START | 177 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `11` | `11` | 180 | START | 180 | 194 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 185 | END | 174 | 185 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 192 | START | 192 | 194 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `21` | 210 | START | 210 | 287 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 313 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–400
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_SnapReceive` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 400 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 168 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 180 | 194 | 15 | inferred_complete_timeline |
| `Action_SplitBlock` | 196 | 313 | 118 | inferred_complete_timeline |
| `Action_None` | 314 | 437 | 124 | inferred_complete_timeline |
| `Action_None` | 441 | 449 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 295 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 212 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 237 | 313 | 77 | inferred_complete_timeline |
| `Action_None` | 314 | 324 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–331
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 289 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 291 | 307 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 312 | 313 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 327 | 14 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 80 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 115 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 158 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 173 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 212 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 260 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 200 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 248 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 237 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 313 | 73 | inferred_complete_timeline |
| `Action_None` | 314 | 330 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 221 | 48 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 253 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 237 | 64 | inferred_complete_timeline |
| `Action_None` | 253 | 291 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 247 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 230 | 57 | inferred_complete_timeline |
| `Action_None` | 232 | 293 | 62 | inferred_complete_timeline |
| `Action_None` | 296 | 328 | 33 | inferred_complete_timeline |
| `Action_None` | 330 | 354 | 25 | inferred_complete_timeline |
| `Action_None` | 357 | 362 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 284 | 111 | inferred_complete_timeline |
| `Action_None` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_None` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 377 | 70 | inferred_complete_timeline |
| `Action_None` | 381 | 382 | 2 | inferred_complete_timeline |
| `Action_None` | 384 | 449 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 227 | 54 | inferred_complete_timeline |
| `Action_None` | 232 | 252 | 21 | inferred_complete_timeline |
| `Action_None` | 271 | 282 | 12 | inferred_complete_timeline |
| `Action_None` | 316 | 380 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_None` | 174 | 290 | 117 | inferred_complete_timeline |
| `Action_None` | 310 | 353 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–353 | 292 | 8 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–186 | 63 | 9 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 8–329 | 316 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 14–42 | 12 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 178–353 | 161 | 8 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 192–287 | 96 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 197–353 | 149 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 207–329 | 97 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 208–235 | 24 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 234–307 | 63 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 295–353 | 53 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 299–353 | 55 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 311–328 | 18 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 316–353 | 27 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 337–382 | 39 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 339–384 | 38 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 340–392 | 53 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 340–353 | 14 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 340–353 | 14 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 346–384 | 39 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 354–403 | 50 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 354–376 | 23 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 354–415 | 62 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 354–386 | 33 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 354–403 | 50 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 354–400 | 47 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 354–449 | 96 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 355–373 | 19 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 355–446 | 77 | 4 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 356–395 | 40 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 360–384 | 25 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 372–445 | 70 | 3 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 409–410 | 2 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 419–420 | 2 | 1 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 431–447 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 138 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 334: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 137 frames exceeds threshold 90 frames [start=177, end=313].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 137 frames exceeds threshold 90 frames [start=177, end=313].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 137 frames exceeds threshold 90 frames [start=177, end=313].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [174–185], lower_priority='Action_ZoneBlock' annotated_start=177, effective_Action_ZoneBlock_start=186.
- ⚠️ Action 'Action_None' range [174-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-282] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-380] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-377] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-353] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-247] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-227] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-353] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [192-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-400] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-289] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [291-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [312-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-328] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-354] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [180-194] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [196-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-437] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-449] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-330] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-212] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [237-313] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-324] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-80] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-115] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-158] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [174-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-212] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-171] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-267] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-31] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-229] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-277] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-353] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [210-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-353] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-293] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-227] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-270] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-324] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-353] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-353] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-353] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-342] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-382] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-384] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-392] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-353] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-353] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-384] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-403] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-376] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-415] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-386] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-403] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-400] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-373] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-425] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-395] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-384] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-377] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-402] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-445] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-447] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>