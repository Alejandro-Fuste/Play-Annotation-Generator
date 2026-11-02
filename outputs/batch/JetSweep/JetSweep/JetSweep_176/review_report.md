# Play-Annotation-Generator Annotation Review — JetSweep_176

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_176`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 45
- **Ball Tracks:** 1
- **Action Segments:** 120
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 138 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `16` | `14` | 136 | START | 136 | 158 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 141 | START | 141 | 152 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `10` | `9` | 143 | START | 143 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 143 | START | 143 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 143 | START | 153 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 143 | START | 143 | 160 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 143 | START | 143 | 171 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 152 | END | 141 | 152 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 155 | START | 155 | 158 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `16` | `14` | 159 | START | 159 | 203 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 171 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_Toss` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_None` | 159 | 187 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 164 | 24 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_LeadBlock` | 143 | 156 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 142 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 171 | 29 | inferred_complete_timeline |
| `Action_None` | 172 | 228 | 57 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_None` | 239 | 258 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 142 | 114 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 169 | 27 | inferred_complete_timeline |
| `Action_None` | 180 | 217 | 38 | inferred_complete_timeline |
| `Action_None` | 228 | 231 | 4 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 43 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 140 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 152 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 171 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 171 | 1 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 189 | 11 | inferred_complete_timeline |
| `Action_None` | 198 | 231 | 34 | inferred_complete_timeline |
| `Action_None` | 245 | 252 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 209 | 69 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 196 | 56 | inferred_complete_timeline |
| `Action_None` | 200 | 222 | 23 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 213 | 73 | inferred_complete_timeline |
| `Action_None` | 216 | 231 | 16 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–261 | 158 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 4–254 | 215 | 4 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 19–203 | 185 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 136–169 | 26 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 150–193 | 44 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 157–245 | 83 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 158–191 | 34 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 165–169 | 5 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 167–237 | 66 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 173–189 | 17 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 188–231 | 40 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 190–298 | 50 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 195–236 | 42 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 199–243 | 24 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 222–245 | 23 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 232–242 | 10 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 238–245 | 8 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 242–245 | 4 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 243–249 | 5 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 253–315 | 63 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 255–256 | 2 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 257–289 | 33 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 260–329 | 56 | 3 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 263–298 | 34 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 310–329 | 19 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 311–328 | 15 | 2 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `42` | `57` | 308 | 308 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 354: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [141–152], lower_priority='Action_ZoneBlock' annotated_start=143, effective_Action_ZoneBlock_start=153.
- ⚠️ Action 'Action_None' range [141-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-222] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-106] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-142] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-228] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-187] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [143-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-169] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-76] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-109] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-115] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '12' starts at frame 153, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [153-164] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-171] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-7] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-231] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-191] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-315] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-289] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-302] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-313] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-298] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-314] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>