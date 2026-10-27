# Play-Annotation-Generator Annotation Review — Counter_274

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_274`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 43
- **Ball Tracks:** 3
- **Action Segments:** 124
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 34 | START | 34 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 37 | START | 37 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `8` | `7` | 37 | START | 37 | 53 |
| ✅ EXACT | `Action_PullBlock` | LG | `7` | `6` | 37 | START | 37 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `18` | `16` | 37 | START | 45 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 52 | END | 34 | 52 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 66 | START | 66 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `16` | 81 | START | 81 | 224 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 98 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–128
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_None` | 53 | 65 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 93 | 128 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 89 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 99 | 107 | 9 | inferred_complete_timeline |
| `Action_None` | 109 | 169 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 99 | 66 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PullBlock` | 37 | 53 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 52 | 19 | inferred_complete_timeline |
| `Action_None` | 53 | 67 | 15 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 56 | 74 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 98 | 1 | inferred_complete_timeline |
| `Action_None` | 99 | 116 | 18 | inferred_complete_timeline |
| `Action_None` | 118 | 149 | 32 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 81 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 67 | 34 | inferred_complete_timeline |
| `Action_None` | 75 | 252 | 178 | inferred_complete_timeline |
| `Action_None` | 254 | 307 | 54 | inferred_complete_timeline |
| `Action_None` | 310 | 317 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 81 | 48 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 171 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 75 | 42 | inferred_complete_timeline |
| `Action_None` | 88 | 167 | 80 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |
| `Action_None` | 196 | 337 | 142 | inferred_complete_timeline |
| `Action_None` | 341 | 345 | 5 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 169 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 119 | 86 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 102 | 69 | inferred_complete_timeline |
| `Action_None` | 104 | 359 | 256 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–306 | 198 | 7 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–155 | 141 | 8 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 42–111 | 48 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 45–349 | 299 | 4 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 71–177 | 100 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 93–107 | 15 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 119–243 | 116 | 2 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 126–159 | 34 | 1 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 131–171 | 41 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 138–346 | 150 | 4 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 150–167 | 18 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 152–315 | 159 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 156–328 | 173 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 199–297 | 80 | 5 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 200–214 | 10 | 4 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 212–303 | 90 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 215–358 | 140 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 225–317 | 93 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 230–286 | 55 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 231–284 | 54 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 232–359 | 128 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 233–359 | 127 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 233–335 | 103 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 235–330 | 95 | 2 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 239–315 | 77 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 244–356 | 108 | 2 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 249–270 | 22 | 1 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 269–359 | 89 | 3 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 335–359 | 23 | 2 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 345–359 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `26` | `37` | 181 | 181 | 1 | 100.0% | None |
| `27` | `38` | 192 | 198 | 6 | 85.7% | 195 |
| `30` | `44` | 202 | 202 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [34-119] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-337] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-345] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [56-74] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-149] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-99] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [37-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-81] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-67] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-252] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-307] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-317] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [45-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [63-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-224] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-349] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-330] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-303] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-315] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-328] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-351] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-317] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-264] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-286] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-335] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-297] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-330] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-315] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-356] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-298] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-351] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-344] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>