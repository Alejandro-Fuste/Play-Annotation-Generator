# Play-Annotation-Generator Annotation Review — Power_197

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_197`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 56
- **Ball Tracks:** 1
- **Action Segments:** 170
- **Validation Warnings:** 235
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | `15` | `15` | 64 | START | 64 | 83 |
| ✅ EXACT | `Action_DownBlock` | RG | `17` | `17` | 64 | START | 64 | 105 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `21` | `21` | 64 | START | 64 | 105 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 236 | 131 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 89 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 150 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 299 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 238 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 105 | 42 | inferred_complete_timeline |
| `Action_None` | 106 | 263 | 158 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 128 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 167 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 200 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 258 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 290 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 230 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 247 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 278 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 168 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 176 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 225 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 239 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 251 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 223 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 261 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 269 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 275 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–299 | 299 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–245 | 240 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–299 | 269 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–181 | 144 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–299 | 295 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–286 | 254 | 9 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 24–33 | 7 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 81–299 | 189 | 7 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 86–145 | 29 | 6 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 96–118 | 19 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 97–244 | 141 | 4 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 102–208 | 17 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 110–177 | 46 | 3 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 127–134 | 8 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 127–139 | 5 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 129–177 | 47 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 131–136 | 6 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 131–136 | 4 | 2 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 140–299 | 137 | 4 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 145–155 | 10 | 2 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 147–149 | 3 | 1 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 169–209 | 10 | 3 | Undefined position; Undefined team |
| `40` | `65` | Position_Unknown | Team_Unknown | 173–299 | 127 | 1 | Undefined position; Undefined team |
| `41` | `68` | Position_Unknown | Team_Unknown | 188–299 | 71 | 6 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 192–299 | 38 | 5 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 217–276 | 25 | 3 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `45` | `75` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 258–265 | 8 | 1 | Undefined position; Undefined team |
| `47` | `80` | Position_Unknown | Team_Unknown | 263–275 | 13 | 1 | Undefined position; Undefined team |
| `48` | `81` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `49` | `82` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `50` | `84` | Position_Unknown | Team_Unknown | 281–291 | 6 | 3 | Undefined position; Undefined team |
| `51` | `85` | Position_Unknown | Team_Unknown | 282–298 | 15 | 2 | Undefined position; Undefined team |
| `52` | `86` | Position_Unknown | Team_Unknown | 282–284 | 3 | 1 | Undefined position; Undefined team |
| `53` | `89` | Position_Unknown | Team_Unknown | 286–299 | 12 | 2 | Undefined position; Undefined team |
| `54` | `90` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `55` | `91` | Position_Unknown | Team_Unknown | 294–299 | 4 | 2 | Undefined position; Undefined team |
| `56` | `92` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `38` | `63` | 168 | 299 | 78 | 59.1% | 175–223, 226–230 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (5 segments found)

### Track Identity Issues

- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 153 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 395: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-280] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-261] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-140] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-168] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-238] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-128] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-167] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-200] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-258] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-89] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-150] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-236] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-263] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-247] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-278] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-102] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-126] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-141] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-92] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-33] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-107] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-114] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-257] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-299] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-103] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-108] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-118] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-236] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-133] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-136] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-143] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-233] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-155] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-224] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-245] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-216] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-231] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-258] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-276] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-227] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-265] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-275] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-286] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-298] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-284] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-294] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>