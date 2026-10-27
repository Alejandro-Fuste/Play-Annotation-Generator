# Play-Annotation-Generator Annotation Review — Counter_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_106`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 174
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 111
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `2` | `1` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 197 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `10` | `9` | 188 | START | 188 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `3` | `2` | 190 | START | 190 | 264 |
| ✅ EXACT | `Action_DownBlock` | LG | `5` | `4` | 190 | START | 190 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `2` | `1` | 190 | START | 190 | 239 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `18` | `17` | 190 | START | 190 | 284 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `4` | `3` | 198 | START | 198 | 234 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 200 | END | 188 | 200 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 216 | START | 216 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 235 | START | 235 | 467 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 284 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_SnapReceive` | 188 | 200 | 13 | inferred_complete_timeline |
| `Action_None` | 201 | 215 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 216 | 234 | 19 | inferred_complete_timeline |
| `Action_None` | 235 | 319 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 198 | 234 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 467 | 233 | inferred_complete_timeline |
| `Action_BallCarry` | 470 | 479 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 264 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_None` | 294 | 302 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_DownBlock` | 190 | 218 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 187 | 118 | inferred_complete_timeline |
| `Action_BallSnap` | 188 | 190 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 192 | 200 | 9 | inferred_complete_timeline |
| `Action_None` | 201 | 356 | 156 | inferred_complete_timeline |
| `Action_None` | 359 | 479 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_PullBlock` | 190 | 239 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 241 | 284 | 44 | inferred_complete_timeline |
| `Action_None` | 285 | 305 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 302 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 245 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 287 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 71 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 151 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 187 | 30 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 274 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |
| `Action_None` | 242 | 301 | 60 | inferred_complete_timeline |
| `Action_None` | 305 | 479 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 237 | 50 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 247 | 266 | 20 | inferred_complete_timeline |
| `Action_None` | 289 | 314 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_None` | 188 | 213 | 26 | inferred_complete_timeline |
| `Action_None` | 215 | 223 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 28 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 108 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 4–81 | 60 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 82–85 | 4 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 97–391 | 295 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 134–304 | 165 | 3 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 154–254 | 38 | 7 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 177–192 | 7 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 214–265 | 4 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 224–299 | 71 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 252–290 | 17 | 4 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 264–346 | 82 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 264–376 | 112 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 274–462 | 189 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 281–337 | 56 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 295–314 | 12 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 307–479 | 169 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 312–405 | 93 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 314–381 | 67 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 330–479 | 150 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 337–340 | 4 | 1 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 385–479 | 95 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 398–403 | 6 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 407–466 | 36 | 8 | Undefined position; Undefined team |
| `37` | `59` | Position_Unknown | Team_Unknown | 413–415 | 3 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 420–479 | 50 | 3 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 420–423 | 4 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 431–479 | 49 | 1 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 442–446 | 5 | 1 | Undefined position; Undefined team |
| `42` | `67` | Position_Unknown | Team_Unknown | 447–448 | 2 | 1 | Undefined position; Undefined team |
| `43` | `69` | Position_Unknown | Team_Unknown | 468–473 | 5 | 2 | Undefined position; Undefined team |
| `44` | `70` | Position_Unknown | Team_Unknown | 473–475 | 3 | 1 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 474–479 | 6 | 1 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 95 frames exceeds threshold 90 frames [start=190, end=284].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '2' (LT) duration 95 frames exceeds threshold 90 frames [start=190, end=284].
- ⚠️ Action 'Action_None' range [188-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [190-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-305] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-264] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [267-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-302] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-467] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [190-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-266] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-287] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '9' starts at frame 188, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [188-190] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-356] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-274] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-301] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-479] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-151] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-70] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-85] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-391] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-294] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-262] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-362] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-376] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-462] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-337] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-314] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-405] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-368] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-381] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-479] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-403] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-414] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-428] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-437] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-466] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-439] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-423] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-446] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-473] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '44' has 1 frames without a visible bounding box.
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

</details>