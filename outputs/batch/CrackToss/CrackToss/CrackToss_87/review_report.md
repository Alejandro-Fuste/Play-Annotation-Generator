# Play-Annotation-Generator Annotation Review — CrackToss_87

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_87`
- **Frame Range:** 0 to 399 (400 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 399
- **Player Tracks:** 58
- **Ball Tracks:** 2
- **Action Segments:** 125
- **Validation Warnings:** 187
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | RB1 | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `29` | `25` |
| ✅ EXACT | `Action_Toss` | RB1 | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB1 | offense | `11` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `1` | `Group` | 0 | START | 0 | 145 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `11` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 151 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 152 | START | 152 | 155 |
| ✅ EXACT | `Action_PullBlock` | RT | `3` | `2` | 155 | START | 155 | 175 |
| ✅ EXACT | `Action_SnapReceive` | RB1 | `11` | `10` | 155 | END | 152 | 155 |
| ⚠️ START CHANGED | `Action_CrackBlock` | Position_Unknown | `29` | `25` | 160 | START | 166 | 200 |
| ✅ EXACT | `Action_Toss` | RB1 | `11` | `10` | 162 | START | 162 | 183 |
| ✅ EXACT | `Action_BallCarry` | RB1 | `11` | `10` | 184 | START | 184 | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_SnapReceive` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 161 | 6 | inferred_complete_timeline |
| `Action_Toss` | 162 | 183 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 194 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_None` | 164 | 201 | 38 | inferred_complete_timeline |
| `Action_None` | 203 | 215 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 187 | 36 | inferred_complete_timeline |
| `Action_None` | 192 | 203 | 12 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 285 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 151 | 103 | inferred_complete_timeline |
| `Action_None` | 152 | 190 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_BallSnap` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 240 | 85 | inferred_complete_timeline |
| `Action_None` | 242 | 250 | 9 | inferred_complete_timeline |
| `Action_None` | 252 | 300 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PullBlock` | 155 | 175 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 399 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 231 | 80 | inferred_complete_timeline |
| `Action_None` | 233 | 315 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 151 | 125 | inferred_complete_timeline |
| `Action_None` | 152 | 233 | 82 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 142 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 315 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 273 | 122 | inferred_complete_timeline |
| `Action_None` | 278 | 319 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 315 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 315 | 164 | inferred_complete_timeline |
| `Action_None` | 342 | 345 | 4 | inferred_complete_timeline |
| `Action_None` | 351 | 396 | 46 | inferred_complete_timeline |
| `Action_None` | 398 | 399 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–15 | 16 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–309 | 299 | 4 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–185 | 186 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 11–68 | 32 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 52–139 | 88 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 117–190 | 74 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 134–262 | 129 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 142–173 | 32 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 166–200 | 35 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 176–315 | 140 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 178–259 | 82 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 201–216 | 16 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 206–229 | 24 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 208–315 | 108 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 224–295 | 64 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 226–347 | 122 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 230–315 | 86 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 236–314 | 79 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 246–315 | 70 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 277–315 | 39 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 278–399 | 103 | 6 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 296–399 | 98 | 4 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 297–315 | 19 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 312–315 | 4 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 312–326 | 6 | 2 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 316–320 | 5 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 316–394 | 79 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 316–399 | 84 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 316–387 | 72 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 316–323 | 8 | 1 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 316–399 | 84 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 316–341 | 26 | 1 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 316–399 | 84 | 1 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 316–325 | 10 | 1 | Undefined position; Undefined team |
| `53` | `66` | Position_Unknown | Team_Unknown | 316–334 | 18 | 2 | Undefined position; Undefined team |
| `54` | `68` | Position_Unknown | Team_Unknown | 316–317 | 2 | 1 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 316–399 | 72 | 5 | Undefined position; Undefined team |
| `56` | `70` | Position_Unknown | Team_Unknown | 317–332 | 14 | 3 | Undefined position; Undefined team |
| `57` | `71` | Position_Unknown | Team_Unknown | 317–325 | 8 | 2 | Undefined position; Undefined team |
| `58` | `74` | Position_Unknown | Team_Unknown | 336–340 | 5 | 1 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 366–399 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 0 | 45 | 46 | 100.0% | None |
| `22` | `24` | 118 | 150 | 32 | 97.0% | 119 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CrackBlock` for actor_track_id `29` (Position_Unknown): Annotated start 160 != Inferred start 166

### Track Identity Issues

- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 204 targets track ID '230', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 100 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [155-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-273] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-319] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-315] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-309] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-187] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [184-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-190] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-285] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-345] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-396] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-240] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-250] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-300] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-36] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-173] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [166-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-315] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-259] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-315] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-260] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-295] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-347] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-315] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-315] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-315] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-315] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-347] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-375] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-385] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-308] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-348] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-315] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-394] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-387] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-323] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-341] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-399] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-325] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-322] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-334] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-372] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-387] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-397] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.

</details>