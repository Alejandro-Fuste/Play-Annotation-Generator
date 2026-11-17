# Play-Annotation-Generator Annotation Review — Power_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_78`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 20 | START | 20 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 20 | START | 20 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 20 | START | 20 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 20 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 20 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 20 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 20 | START | 20 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 20 | START | 20 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `13` | 46 | START | 46 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `14` | 46 | START | 46 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `4` | 46 | START | 46 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `3` | 46 | START | 46 | 70 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 20–261
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 71 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 123 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 253 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 261 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 71 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 89 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 329 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 120 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 148 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 156 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 329 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 20–298
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 266 | 169 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |
| `Action_None` | 273 | 298 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–326
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 100 | 117 | 18 | inferred_complete_timeline |
| `Action_None` | 119 | 305 | 187 | inferred_complete_timeline |
| `Action_None` | 308 | 326 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–280
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 82 | 31 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 192 | 29 | inferred_complete_timeline |
| `Action_None` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 266 | 53 | inferred_complete_timeline |
| `Action_None` | 273 | 276 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 280 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 46 | 70 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 77 | 97 | 21 | inferred_complete_timeline |
| `Action_None` | 98 | 110 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 131 | 9 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–156
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 147 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 156 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 125 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 329 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–294
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 136 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 294 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–95
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 95 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–312
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 142 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 294 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 303 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 312 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 114 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 237 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 294 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 314 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 329 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 329 | 310 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 20–293 | 267 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 74–300 | 219 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 81–329 | 244 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 97–294 | 191 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 109–317 | 194 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 120–329 | 210 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 158–329 | 172 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 206–329 | 124 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 223–226 | 4 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 245–255 | 11 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 301–304 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-114] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-294] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-294] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [46-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-266] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-298] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-142] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-294] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-156] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-125] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-226] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-293] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-71] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-89] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-120] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-156] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-49] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-192] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-266] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-79] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-326] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-296] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-300] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-314] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-265] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-283] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-291] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-258] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-288] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-303] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-309] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-317] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-255] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>