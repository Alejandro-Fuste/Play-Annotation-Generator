# Play-Annotation-Generator Annotation Review — Power_219

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_219`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 4 | START | 4 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 4 | START | 4 | 304 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 4 | START | 4 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 4 | START | 4 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 4 | START | 4 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 4 | START | 4 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 4 | START | 4 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 4 | START | 4 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 4 | START | 4 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 4 | START | 4 | 270 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 4 | START | 4 | 384 |
| ✅ EXACT | `Action_DownBlock` | LG | `2` | `2` | 205 | START | 205 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `20` | `20` | 205 | START | 205 | 223 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `21` | 205 | START | 205 | 232 |

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
- **Visible Frames:** 4–384
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 384 | 381 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–442
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 270 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 430 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 436 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 441 | 442 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 432 | 429 | inferred_complete_timeline |
| `Action_PreSnap` | 434 | 437 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 449 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 304 | 301 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 449 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 449 | 446 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–422
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 422 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–449
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 204 | 201 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 223 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 249 | 18 | inferred_complete_timeline |
| `Action_None` | 250 | 268 | 19 | inferred_complete_timeline |
| `Action_None` | 271 | 449 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 204 | 201 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 249 | 45 | inferred_complete_timeline |
| `Action_None` | 250 | 449 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–278
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 208 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 230 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 266 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 278 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–253
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 204 | 201 | inferred_complete_timeline |
| `Action_PullBlock` | 205 | 232 | 28 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 389 | 386 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–385
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 308 | 305 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 385 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–208
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 208 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–268
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 245 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–272
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 248 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 261 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 272 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 259 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 272 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 297 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 449 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 449 | 446 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–356
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 253 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 269 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 356 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 449 | 446 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 449 | 446 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–449
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 446 | 443 | inferred_complete_timeline |
| `Action_PreSnap` | 448 | 449 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 4–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 449 | 446 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 232–234 | 3 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 246–449 | 185 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 253–264 | 11 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 268–420 | 151 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 281–449 | 169 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 288–401 | 114 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 289–431 | 143 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 361–362 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 48 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [4-304] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-432] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-437] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-385] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-270] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-430] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-436] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-442] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-384] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-278] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-446] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-422] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-356] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [205-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-249] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-449] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [205-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-449] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-261] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-332] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-420] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-401] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-431] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '29' has 1 frames without a visible bounding box.
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

</details>