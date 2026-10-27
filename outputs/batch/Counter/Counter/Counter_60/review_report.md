# Play-Annotation-Generator Annotation Review — Counter_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_60`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `12` | `11` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 173 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 171 | START | 171 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 174 | START | 189 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 174 | START | 174 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `7` | 176 | START | 176 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `12` | `11` | 176 | START | 176 | 202 |
| ✅ EXACT | `Action_SnapReceive` | RB | `7` | `6` | 188 | END | 171 | 188 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 214 | START | 214 | 246 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 254 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 202 | 32 | inferred_complete_timeline |
| `Action_None` | 212 | 236 | 25 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 170 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 189 | 213 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 246 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 176 | 202 | 27 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 205 | 213 | 9 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 222 | 254 | 33 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 297 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 249 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 337 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 191 | 21 | inferred_complete_timeline |
| `Action_None` | 196 | 275 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_BallSnap` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 189 | 202 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PullBlock` | 176 | 198 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 253 | 83 | inferred_complete_timeline |
| `Action_None` | 256 | 270 | 15 | inferred_complete_timeline |
| `Action_None` | 287 | 294 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 290 | 120 | inferred_complete_timeline |
| `Action_None` | 301 | 419 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 287 | 117 | inferred_complete_timeline |
| `Action_None` | 296 | 311 | 16 | inferred_complete_timeline |
| `Action_None` | 318 | 419 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 325 | 155 | inferred_complete_timeline |
| `Action_None` | 327 | 348 | 22 | inferred_complete_timeline |
| `Action_None` | 351 | 419 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 219 | 49 | inferred_complete_timeline |
| `Action_None` | 221 | 231 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 316 | 146 | inferred_complete_timeline |
| `Action_None` | 318 | 335 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 331 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_None` | 171 | 228 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 116–237 | 122 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 210–335 | 112 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 245–329 | 85 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 249–298 | 50 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 252–332 | 51 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 264–419 | 153 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 288–419 | 128 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 300–419 | 120 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 303–419 | 117 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 305–412 | 88 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 305–419 | 105 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 311–407 | 95 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 316–359 | 44 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 322–419 | 98 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 323–419 | 97 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 328–419 | 86 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 329–419 | 91 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 346–419 | 74 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 353–354 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 365–391 | 17 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 379–419 | 41 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 391–419 | 29 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 416–419 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `12` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [171–188], lower_priority='Action_DownBlock' annotated_start=174, effective_Action_DownBlock_start=189.
- ⚠️ Action 'Action_None' range [171-331] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-316] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-325] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-348] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-419] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-290] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [176-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [236-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-337] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-275] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [176-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [205-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-297] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-202] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [205-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-231] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-284] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-335] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-332] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-398] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-338] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-412] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-322] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-368] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-407] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-359] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-354] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-372] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-381] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-419] for track '36' has 2 frames without a visible bounding box.
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

</details>