# Play-Annotation-Generator Annotation Review — Power_226

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_226`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | DT2 | defense | `18` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `16` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 8 | START | 8 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 8 | START | 8 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 8 | START | 8 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 8 | START | 8 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 8 | START | 8 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 8 | START | 20 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 8 | START | 8 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 8 | START | 8 | 24 |
| ✅ EXACT | `Action_DownBlock` | DT2 | `18` | `16` | 264 | START | 264 | 303 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `9` | 264 | START | 264 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `16` | `15` | 264 | START | 264 | 275 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 8–381
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 26 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 381 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–419
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 50 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 181 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 205 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 233 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 340 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–167
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 85 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 151 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 167 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 8–419
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 153 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 343 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 419 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–358
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 12 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 22 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 217 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 338 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 358 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 8–361
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 24 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 36 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 202 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 263 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 290 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 293 | 309 | 17 | inferred_complete_timeline |
| `Action_None` | 310 | 361 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 20–419
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 178 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 263 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 264 | 275 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 281 | 309 | 29 | inferred_complete_timeline |
| `Action_None` | 310 | 419 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 62 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 419 | 344 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 8–419
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 125 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 275 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 419 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 71–356
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 71 | 169 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 189 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 263 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 303 | 40 | inferred_complete_timeline |
| `Action_None` | 353 | 356 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 33 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 313 | 278 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 360 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 419 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–298
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 42 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 259 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 273 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 298 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–144
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 89 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 144 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–297
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 294 | 287 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 8–78 | 71 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 8–55 | 47 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 8–72 | 54 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 161–419 | 256 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 178–419 | 179 | 5 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 266–419 | 88 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 267–372 | 91 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 278–313 | 16 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 286–419 | 76 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 299–330 | 26 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 308–419 | 79 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 310–419 | 73 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 313–333 | 21 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 331–387 | 46 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 334–384 | 51 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 361–389 | 29 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 375–399 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 91 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [8-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-73] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-275] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-33] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-313] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-360] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-259] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-85] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-50] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [264-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [293-309] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-181] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-340] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-26] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-381] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-40] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-343] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-338] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [264-275] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-169] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-189] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [264-303] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-370] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-419] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-315] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-387] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-276] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-354] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-372] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-289] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-332] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-317] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-323] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-317] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-373] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-316] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-350] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-399] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-333] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-366] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-387] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-384] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-389] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-399] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>