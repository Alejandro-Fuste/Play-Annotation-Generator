# Play-Annotation-Generator Annotation Review — CrackToss_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_85`
- **Frame Range:** 0 to 349 (350 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 349
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 83
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `26` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `29` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `23` | `22` |
| ✅ EXACT | `Action_Toss` | QB | offense | `23` | `22` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `26` | `25` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 8 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 8 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 8 | START | 0 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 8 | START | 8 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `23` | `Group` | 8 | START | 8 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `25` | `Group` | 8 | START | 8 | 241 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `26` | `Group` | 8 | START | 8 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 242 | START | 242 | 253 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `29` | `28` | 245 | START | 245 | 308 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `12` | `11` | 245 | START | 245 | 260 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `14` | `13` | 245 | START | 254 | 280 |
| ✅ EXACT | `Action_SnapReceive` | QB | `23` | `22` | 253 | END | 242 | 253 |
| ✅ EXACT | `Action_Toss` | QB | `23` | `22` | 257 | START | 257 | 275 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `26` | `25` | 276 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 324 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 8–311
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_SnapReceive` | 242 | 253 | 12 | inferred_complete_timeline |
| `Action_None` | 254 | 256 | 3 | inferred_complete_timeline |
| `Action_Toss` | 257 | 275 | 19 | inferred_complete_timeline |
| `Action_None` | 276 | 307 | 32 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `26`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 8–34
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 34 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_PullBlock` | 245 | 260 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 262 | 324 | 63 | inferred_complete_timeline |
| `Action_None` | 325 | 339 | 15 | inferred_complete_timeline |
| `Action_None` | 344 | 349 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_None` | 242 | 253 | 12 | inferred_complete_timeline |
| `Action_None` | 271 | 273 | 3 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 291 | 4 | inferred_complete_timeline |
| `Action_None` | 339 | 349 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_BallSnap` | 242 | 253 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 254 | 280 | 27 | inferred_complete_timeline |
| `Action_PullBlock` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 291 | 311 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 313 | 324 | 12 | inferred_complete_timeline |
| `Action_None` | 325 | 349 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 8–349
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 349 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 8–259
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 259 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 8–349
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 273 | 32 | inferred_complete_timeline |
| `Action_None` | 275 | 349 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 8–318
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 263 | 22 | inferred_complete_timeline |
| `Action_None` | 266 | 304 | 39 | inferred_complete_timeline |
| `Action_None` | 315 | 318 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 241 | 235 | inferred_complete_timeline |
| `Action_None` | 242 | 349 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 8–349
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 349 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 8–349
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 349 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 241 | 242 | inferred_complete_timeline |
| `Action_None` | 242 | 333 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `27`</summary>

- **xml_track_id:** `26`
- **actor_track_id:** `27`
- **team_side:** `defense`
- **Visible Frames:** 8–349
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 241 | 234 | inferred_complete_timeline |
| `Action_None` | 242 | 258 | 17 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 349 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 34–349 | 316 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 39–349 | 310 | 4 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 42–349 | 306 | 3 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 78–335 | 258 | 2 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 82–349 | 268 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 268–349 | 79 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 269–349 | 80 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 278–345 | 68 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 286–337 | 49 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 342–349 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `32` | `35` | 125 | 142 | 15 | 83.3% | 126, 130–131 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `29` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `26` (RB)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 349 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [242–253], lower_priority='Action_PullBlock' annotated_start=245, effective_Action_PullBlock_start=254.
- ⚠️ Segment 'Action_BallCarry' for track '25' has invalid range: start=276, end=34. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-333] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [245-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-339] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [254-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [285-288] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [291-311] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-349] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-307] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-349] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-34] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-241] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [245-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [310-324] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-325] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-335] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-292] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-294] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-337] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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