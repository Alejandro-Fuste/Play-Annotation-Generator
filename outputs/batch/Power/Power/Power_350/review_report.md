# Play-Annotation-Generator Annotation Review — Power_350

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_350`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 19 | START | 19 | 250 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 19 | START | 19 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 19 | START | 19 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 19 | START | 19 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 19 | START | 19 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 19 | START | 19 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `8` | `Group` | 19 | START | 19 | 323 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `12` | 232 | START | 232 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `7` | `7` | 232 | START | 232 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `4` | `4` | 232 | START | 232 | 242 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–306
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 239 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 306 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 19–449
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 323 | 305 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 347 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 365 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 401 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 426 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 449 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 19–332
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 319 | 301 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 327 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 332 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 19–368
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 231 | 213 | inferred_complete_timeline |
| `Action_PullBlock` | 232 | 242 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 246 | 297 | 52 | inferred_complete_timeline |
| `Action_None` | 298 | 368 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 19–449
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 231 | 213 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 239 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 246 | 261 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 283 | 292 | 10 | inferred_complete_timeline |
| `Action_None` | 301 | 434 | 134 | inferred_complete_timeline |
| `Action_None` | 438 | 441 | 4 | inferred_complete_timeline |
| `Action_None` | 449 | 449 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 19–281
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 250 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 270 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 281 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 19–360
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 231 | 213 | inferred_complete_timeline |
| `Action_DownBlock` | 232 | 262 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 297 | 34 | inferred_complete_timeline |
| `Action_None` | 298 | 360 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 19–449
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 292 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 346 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 449 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 19–350
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 266 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 350 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 19–231
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 90 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 231 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–449
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 235 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 449 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 19–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 338 | 320 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 449 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 19–234
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 234 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 19–405 | 384 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 219–226 | 8 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 233–284 | 42 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 244–276 | 33 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 256–449 | 191 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 285–449 | 160 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 291–421 | 124 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 311–449 | 126 | 4 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 315–449 | 116 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 318–352 | 35 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 335–449 | 97 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 340–391 | 48 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 341–374 | 31 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 347–446 | 85 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 352–447 | 80 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 396–449 | 50 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [19-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-281] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-338] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-449] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-292] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-346] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [232-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-368] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-306] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-319] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-332] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-360] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-347] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-365] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-401] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-426] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-350] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-90] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-449] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [232-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [242-243] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [246-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [278-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [283-292] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-434] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-441] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-405] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-284] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-276] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-378] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-422] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-371] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-411] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-421] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-378] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-397] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-406] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-336] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-352] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-373] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-388] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [391-410] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-365] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-391] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-353] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-358] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-371] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-362] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-381] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-417] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-446] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-374] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-393] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-439] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-447] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-400] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>