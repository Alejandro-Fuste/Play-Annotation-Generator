# Play-Annotation-Generator Annotation Review — Power_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_46`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 25 | START | 25 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 25 | START | 25 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 25 | START | 25 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 25 | START | 25 | 313 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 25 | START | 25 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 25 | START | 25 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 175 | START | 175 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `16` | `16` | 175 | START | 180 | 195 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–281
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 203 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 268 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 25–53
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 40 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 53 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 25–326
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 182 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 219 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 280 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 326 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 174 | 150 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 199 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 207 | 243 | 37 | inferred_complete_timeline |
| `Action_None` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–206
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 77 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 172 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 25–313
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 313 | 289 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 25–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 329 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–310
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 274 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 310 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 25–232
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 67 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 75 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 232 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 25–232
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 219 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 232 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–205
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 45 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 79 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 201 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 205 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 25–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 329 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 25–325
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 183 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 313 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 325 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 170–308 | 126 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 172–203 | 32 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 174–205 | 28 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 180–242 | 59 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 210–316 | 93 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 219–329 | 103 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 238–296 | 59 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 239–329 | 91 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 241–329 | 82 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 246–250 | 5 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 251–262 | 12 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 254–278 | 25 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 259–329 | 57 | 5 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 260–309 | 35 | 5 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 279–323 | 43 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 302–329 | 27 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 302–304 | 3 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 303–314 | 12 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 310–329 | 18 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 324–327 | 4 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 84 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [25-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-313] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-172] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-232] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-274] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-310] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-313] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-268] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [207-243] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-219] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-280] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-326] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-53] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-79] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-205] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-202] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-308] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-199] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [180-195] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [198-223] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [226-242] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-300] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-316] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-253] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-315] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-296] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-281] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-304] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-323] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-278] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-284] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-302] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-270] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-317] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-323] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-316] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-304] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-314] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-325] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '37' has 1 frames without a visible bounding box.
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

</details>