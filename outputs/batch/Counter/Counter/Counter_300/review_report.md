# Play-Annotation-Generator Annotation Review — Counter_300

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_300`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 85
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 108 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 106 | START | 106 | 120 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `11` | `10` | 109 | START | 121 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `13` | `12` | 109 | START | 109 | 113 |
| ✅ EXACT | `Action_DownBlock` | RG | `7` | `6` | 109 | START | 109 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `9` | `8` | 109 | START | 109 | 134 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `4` | `3` | 109 | START | 109 | 196 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `5` | `4` | 120 | START | 120 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 120 | END | 106 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `10` | `9` | 129 | START | 129 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 153 | START | 153 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 196 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_SnapReceive` | 106 | 120 | 15 | inferred_complete_timeline |
| `Action_None` | 121 | 128 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 146 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 153 | 204 | 52 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 120 | 152 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 224 | 72 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 337 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 109 | 196 | 88 | inferred_complete_timeline |
| `Action_None` | 197 | 234 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 122 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PullBlock` | 109 | 134 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 138 | 196 | 59 | inferred_complete_timeline |
| `Action_None` | 197 | 221 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_BallSnap` | 106 | 120 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 121 | 196 | 76 | inferred_complete_timeline |
| `Action_None` | 197 | 305 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 124 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 15 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 27 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 108 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 127 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 196 | 68 | inferred_complete_timeline |
| `Action_None` | 197 | 207 | 11 | inferred_complete_timeline |
| `Action_None` | 211 | 219 | 9 | inferred_complete_timeline |
| `Action_None` | 222 | 265 | 44 | inferred_complete_timeline |
| `Action_None` | 267 | 280 | 14 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 147 | 42 | inferred_complete_timeline |
| `Action_None` | 149 | 154 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 183 | 78 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 105 | 26 | inferred_complete_timeline |
| `Action_None` | 106 | 185 | 80 | inferred_complete_timeline |
| `Action_None` | 190 | 276 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 105 | 47 | inferred_complete_timeline |
| `Action_None` | 106 | 204 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 133 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_None` | 106 | 197 | 92 | inferred_complete_timeline |
| `Action_None` | 199 | 216 | 18 | inferred_complete_timeline |
| `Action_None` | 224 | 245 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 23–359 | 336 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 148–359 | 206 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 154–267 | 114 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 170–359 | 180 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 182–280 | 98 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 191–252 | 58 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 200–359 | 160 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 214–256 | 43 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 216–359 | 144 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 236–359 | 124 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 240–359 | 120 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 242–258 | 16 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 276–310 | 32 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 299–359 | 61 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | 198 | 198 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `11` (C): Annotated start 109 != Inferred start 121
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [106–120], lower_priority='Action_DownBlock' annotated_start=109, effective_Action_DownBlock_start=121.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-216] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-105] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-276] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-224] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-337] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-183] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [109-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [138-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [129-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [121-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-305] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-108] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [129-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-207] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-280] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-267] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-280] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-256] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-282] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-298] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-359] for track '28' has 1 frames without a visible bounding box.
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

</details>