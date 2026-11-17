# Play-Annotation-Generator Annotation Review — Power_345

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_345`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

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
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 4 | START | 4 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 4 | START | 4 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 4 | START | 4 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 4 | START | 4 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 4 | START | 4 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 4 | START | 4 | 389 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 4 | START | 4 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 4 | START | 4 | 332 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `3` | `Group` | 4 | START | 4 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 4 | START | 4 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `14` | 185 | START | 185 | 198 |
| ✅ EXACT | `Action_DownBlock` | RG | `20` | `20` | 185 | START | 185 | 218 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RT | `6` | `6` | 185 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | LT | `19` | `19` | 185 | START | 185 | 218 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–220
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 220 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–192
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 192 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 389 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 389 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 389 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 184 | 181 | inferred_complete_timeline |
| `Action_PullBlock` | 185 | 218 | 34 | inferred_complete_timeline |
| `Action_None` | 219 | 389 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–370
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 332 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 370 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–207
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 184 | 181 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 198 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 164 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 184 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 218 | 34 | inferred_complete_timeline |
| `Action_None` | 219 | 389 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–170
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 170 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–382
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 198 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 278 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 295 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 382 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–361
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 252 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 285 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 304 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 328 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 335 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 361 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–385
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 203 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 385 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 324 | 321 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 337 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 383 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 389 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–234
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 234 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–365
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 355 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 365 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 4–350
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 23 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 350 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–347
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 347 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 389 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 232 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 389 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 4–371 | 362 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 202–204 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 206–216 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 212–369 | 143 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 221–225 | 5 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 227–381 | 155 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 245–388 | 144 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 269–371 | 76 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 278–329 | 22 | 7 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 351–352 | 2 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 367–369 | 3 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 374–381 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `6` (RT)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 690: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '6' has invalid range: start=185, end=170. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [4-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-347] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-252] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-285] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-304] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-328] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-335] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-385] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-198] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-295] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-382] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-355] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-365] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-371] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-324] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-383] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-220] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-350] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-389] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-332] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-370] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-369] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-381] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-388] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-336] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-371] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-302] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-369] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-375] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>