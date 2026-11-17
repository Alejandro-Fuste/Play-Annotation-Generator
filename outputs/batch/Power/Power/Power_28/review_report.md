# Play-Annotation-Generator Annotation Review — Power_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_28`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | TE1 | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 24 | START | 24 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 24 | START | 24 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 24 | START | 24 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 24 | START | 24 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 24 | START | 80 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 24 | START | 24 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 24 | START | 24 | 208 |
| ✅ EXACT | `Action_DownBlock` | TE1 | `7` | `7` | 209 | START | 209 | 222 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `9` | 209 | START | 209 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `12` | `12` | 209 | START | 209 | 211 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 24–121
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 121 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 24–259
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 259 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 24–362
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 208 | 185 | inferred_complete_timeline |
| `Action_DownBlock` | 209 | 222 | 14 | inferred_complete_timeline |
| `Action_None` | 270 | 297 | 28 | inferred_complete_timeline |
| `Action_None` | 303 | 305 | 3 | inferred_complete_timeline |
| `Action_None` | 307 | 317 | 11 | inferred_complete_timeline |
| `Action_None` | 319 | 324 | 6 | inferred_complete_timeline |
| `Action_None` | 351 | 362 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 24–247
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 236 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 80–307
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 80 | 115 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 158 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 205 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 221 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 245 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 253 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 307 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 24–389
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 208 | 185 | inferred_complete_timeline |
| `Action_DownBlock` | 209 | 219 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 239 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 256 | 265 | 10 | inferred_complete_timeline |
| `Action_None` | 266 | 277 | 12 | inferred_complete_timeline |
| `Action_None` | 295 | 389 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 208 | 185 | inferred_complete_timeline |
| `Action_PullBlock` | 209 | 211 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 214 | 220 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 224 | 236 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 247 | 265 | 19 | inferred_complete_timeline |
| `Action_None` | 266 | 293 | 28 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–94
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 24–389
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 224 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 244 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 291 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 361 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 365 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 389 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 24–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 363 | 340 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 389 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 24–242
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 242 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 24–367
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 359 | 336 | inferred_complete_timeline |
| `Action_PreSnap` | 362 | 367 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 24–358
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 273 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 293 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 326 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 332 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 358 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 51 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 389 | 325 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 24–389 | 366 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 24–59 | 35 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 29–359 | 275 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 50–77 | 20 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 109–220 | 93 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 113–362 | 176 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 116–389 | 248 | 7 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 175–389 | 199 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 215–389 | 159 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 219–322 | 104 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 247–265 | 14 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 252–353 | 75 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 258–346 | 82 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 271–389 | 115 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 278–286 | 6 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 293–389 | 88 | 5 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 296–389 | 94 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 323–354 | 15 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 345–372 | 25 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 361–375 | 15 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 365–375 | 11 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 383–389 | 6 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 108 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [24-363] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-389] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-367] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-51] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-273] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-358] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-94] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-317] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-362] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-291] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-361] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [209-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-277] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-247] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [209-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [214-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [224-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [242-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [247-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-293] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-259] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-121] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-359] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-115] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-158] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-205] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-166] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-195] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-220] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-170] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-254] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-362] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-152] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-200] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-271] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-332] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-341] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-295] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-289] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-274] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-320] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-353] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-277] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-389] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-281] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-297] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-341] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-375] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-333] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-356] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-372] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-375] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-375] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-386] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>