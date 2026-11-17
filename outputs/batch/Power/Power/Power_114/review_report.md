# Play-Annotation-Generator Annotation Review — Power_114

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_114`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `13` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 22 | START | 22 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 22 | START | 22 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 22 | START | 69 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 22 | START | 22 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 22 | START | 22 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 22 | START | 22 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 22 | START | 22 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 22 | START | 22 | 198 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `11` | `11` | 199 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `13` | `13` | 199 | START | 199 | 203 |
| ✅ EXACT | `Action_DownBlock` | LT | `9` | `9` | 199 | START | 199 | 241 |
| ✅ EXACT | `Action_PullBlock` | RG | `3` | `3` | 199 | START | 199 | 241 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 359 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 236 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 359 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 206 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 359 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 198 | 177 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 241 | 43 | inferred_complete_timeline |
| `Action_None` | 242 | 359 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 219 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 258 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 359 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 69–359
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 69 | 120 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 349 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 359 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–359
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 198 | 177 | inferred_complete_timeline |
| `Action_PullBlock` | 199 | 241 | 43 | inferred_complete_timeline |
| `Action_None` | 242 | 359 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–313
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 214 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 313 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 67–286
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 67 | 200 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 212 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 286 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–274
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 274 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 54–359
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 54 | 198 | 145 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 212 | 217 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 238 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 241 | 241 | 1 | inferred_complete_timeline |
| `Action_None` | 242 | 280 | 39 | inferred_complete_timeline |
| `Action_None` | 285 | 359 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 101 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 142 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 269 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 359 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–256
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 256 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–307
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 214 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 258 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 307 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–359
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 305 | 284 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 348 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 22–56 | 35 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 183–359 | 177 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 193–331 | 108 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 217–259 | 43 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 240–250 | 10 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 245–359 | 112 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 252–253 | 2 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 262–352 | 91 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 263–359 | 97 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 271–359 | 89 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 273–359 | 87 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 284–287 | 4 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 286–359 | 74 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 288–290 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 292–359 | 68 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 295–359 | 59 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 315–359 | 45 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 319–359 | 14 | 5 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `11` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '11' has invalid range: start=199, end=56. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [22-236] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-256] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-274] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-214] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-313] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-214] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-305] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-348] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-142] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-203] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [212-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-238] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-280] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-359] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-286] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-349] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-300] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-292] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-305] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-352] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-315] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-332] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-340] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>