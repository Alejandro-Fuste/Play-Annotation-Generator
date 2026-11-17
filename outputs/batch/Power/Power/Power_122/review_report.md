# Play-Annotation-Generator Annotation Review — Power_122

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_122`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 1
- **Action Segments:** 95
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 0
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE1 | defense | `12` | `12` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 15 | START | 15 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 15 | START | 15 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 15 | START | 15 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 15 | START | 15 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 15 | START | 15 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 15 | START | 15 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 15 | START | 15 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `9` | `Group` | 15 | START | 15 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `11` | `11` | 54 | START | 54 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE1 | `12` | `12` | 54 | START | 54 | 78 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `3` | `3` | 54 | START | 56 | 65 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–153
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 78 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 153 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–85
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 85 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 15–240
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 64 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 84 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 196 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 231 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 240 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–82
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 68 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 82 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 15–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 49 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 80 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 269 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 15–100
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 51 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 100 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–65
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 53 | 39 | inferred_complete_timeline |
| `Action_PullBlock` | 56 | 65 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 15–141
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 53 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 60 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 102 | 29 | inferred_complete_timeline |
| `Action_None` | 103 | 134 | 32 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 15–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 50 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 54 | 78 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 102 | 22 | inferred_complete_timeline |
| `Action_None` | 103 | 269 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 269 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–72
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 72 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 15–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 131 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 130 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 269 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–50
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 50 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 15–236 | 205 | 6 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 15–269 | 254 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 15–133 | 107 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 87–269 | 182 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 99–269 | 139 | 7 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 103–269 | 146 | 5 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 111–133 | 4 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 120–269 | 147 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 138–269 | 128 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 142–269 | 128 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 147–269 | 101 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 150–263 | 114 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 150–269 | 110 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 153–269 | 116 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 155–237 | 66 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 159–269 | 111 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 203–269 | 66 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 226–269 | 29 | 4 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 233–269 | 14 | 3 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 241–256 | 15 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 255–258 | 4 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 256–268 | 13 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 28 | 36 | 6 | 66.7% | 29–31 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `3` (C): Annotated start 54 != Inferred start 56

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 246: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 246: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [15-101] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-131] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-78] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-53] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [56-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-260] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-269] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [54-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-133] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-100] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-269] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-138] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-221] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-222] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-237] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-163] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-256] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-209] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-245] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-254] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-256] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-268] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>