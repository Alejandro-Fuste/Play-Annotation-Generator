# Play-Annotation-Generator Annotation Review — Power_185

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_185`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 187
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 26 | START | 26 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 26 | START | 26 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 26 | START | 26 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 26 | START | 26 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 26 | START | 26 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 26 | START | 26 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 26 | START | 26 | 313 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 26 | START | 26 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 26 | START | 26 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 26 | START | 26 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 26 | START | 26 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `11` | `11` | 80 | START | 80 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `20` | 80 | START | 80 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `16` | `16` | 80 | START | 80 | 88 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 313 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 324 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 26–95
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 95 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 317 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 329 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 26–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 329 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 329 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 26–193
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 102 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 165 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 193 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 26–210
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 129 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 166 | 25 | inferred_complete_timeline |
| `Action_None` | 187 | 210 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 26–178
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 69 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 124 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 139 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 178 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 26–135
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 85 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 130 | 135 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–134
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 134 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 26–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 88 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 114 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 329 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 26–329
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 116 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 159 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 199 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 329 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–114
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 114 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 26–119
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 87 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 100 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–165
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 87 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 165 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 26–329
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 159 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 200 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 277 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–113
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 113 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–168
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 168 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 292 | 267 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 306 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 329 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–306
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 290 | 265 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 302 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 306 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–229
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 179 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 229 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 318 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 323 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 91–109 | 18 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 108–329 | 201 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 111–115 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 115–329 | 179 | 5 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 129–144 | 16 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 147–329 | 145 | 12 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 147–158 | 12 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 154–329 | 156 | 8 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 158–208 | 27 | 5 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 177–329 | 96 | 7 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 185–329 | 145 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 185–329 | 115 | 8 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 189–329 | 141 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 190–329 | 120 | 5 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 192–329 | 128 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 223–241 | 11 | 3 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 275–329 | 53 | 2 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 279–281 | 3 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 295–317 | 13 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 140 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [26-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-200] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-277] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-179] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-229] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-87] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-165] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-292] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-88] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-318] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-102] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-165] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-129] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-136] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-302] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-114] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-145] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-329] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [80-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [90-97] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [99-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-134] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-116] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-159] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-199] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-313] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-324] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [92-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [130-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-124] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-139] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-156] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-102] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-143] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-165] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-270] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-159] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-281] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-144] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-226] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-241] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-180] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-317] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-329] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-179] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-233] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-243] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-292] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-196] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-214] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-268] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-297] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-200] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-211] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-240] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-260] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-196] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-233] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-241] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-278] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-303] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-317] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-329] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>