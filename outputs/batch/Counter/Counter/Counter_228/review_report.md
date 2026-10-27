# Play-Annotation-Generator Annotation Review — Counter_228

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_228`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 78
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_DownBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `16` | `15` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 114 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 111 | START | 111 | 128 |
| ⚠️ START CHANGED | `Action_DownBlock` | RT | `13` | `12` | 112 | START | 114 | 117 |
| ✅ EXACT | `Action_DownBlock` | RG | `17` | `16` | 112 | START | 112 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `7` | `6` | 112 | START | 129 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `11` | `10` | 112 | START | 112 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `16` | `15` | 112 | START | 112 | 148 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `9` | `8` | 115 | START | 115 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 128 | END | 111 | 128 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 139 | START | 139 | 156 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `8` | 157 | START | 157 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 188 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_SnapReceive` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_None` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 139 | 156 | 18 | inferred_complete_timeline |
| `Action_None` | 157 | 182 | 26 | inferred_complete_timeline |
| `Action_None` | 187 | 221 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 115 | 156 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 299 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 112 | 148 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 155 | 188 | 34 | inferred_complete_timeline |
| `Action_None` | 189 | 257 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 157 | 47 | inferred_complete_timeline |
| `Action_None` | 159 | 185 | 27 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 252 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 128 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 133 | 188 | 56 | inferred_complete_timeline |
| `Action_None` | 189 | 235 | 47 | inferred_complete_timeline |
| `Action_None` | 238 | 241 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_BallSnap` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 142 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 188 | 35 | inferred_complete_timeline |
| `Action_None` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_None` | 194 | 245 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 188 | 77 | inferred_complete_timeline |
| `Action_None` | 189 | 245 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 117 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 267 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 176 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 152 | 42 | inferred_complete_timeline |
| `Action_None` | 197 | 224 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 231 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 182 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 228 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_None` | 111 | 299 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 32–128 | 11 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 69–271 | 118 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 71–256 | 183 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 145–198 | 54 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 165–170 | 5 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 191–293 | 103 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 199–243 | 42 | 3 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 207–244 | 37 | 2 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 216–244 | 29 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 223–241 | 8 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 229–246 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `21` | `26` | 145 | 145 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `13` (RT): Annotated start 112 != Inferred start 114
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [111–128], lower_priority='Action_DownBlock' annotated_start=112, effective_Action_DownBlock_start=129.
- ⚠️ Action 'Action_None' range [111-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-231] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [139-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [146-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-176] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-224] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-157] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [112-148] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [150-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-245] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-198] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-293] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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