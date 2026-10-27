# Play-Annotation-Generator Annotation Review — Counter_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_90`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 78 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 77 | START | 77 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 79 | START | 96 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `11` | `10` | 79 | START | 79 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `8` | `7` | 79 | START | 79 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 79 | START | 79 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `14` | `13` | 79 | START | 79 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `5` | `4` | 81 | START | 81 | 156 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 95 | END | 77 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `6` | `5` | 131 | START | 131 | 223 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 95 | 19 | inferred_complete_timeline |
| `Action_None` | 96 | 115 | 20 | inferred_complete_timeline |
| `Action_None` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 223 | 93 | inferred_complete_timeline |
| `Action_BallCarry` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 81 | 156 | 76 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 159 | 163 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 116 | 40 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 143 | 35 | inferred_complete_timeline |
| `Action_None` | 144 | 253 | 110 | inferred_complete_timeline |
| `Action_None` | 255 | 274 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 109 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 126 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 95 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 143 | 37 | inferred_complete_timeline |
| `Action_None` | 144 | 198 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 94 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 106 | 109 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 79 | 129 | 51 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_None` | 144 | 173 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 162 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 119 | 43 | inferred_complete_timeline |
| `Action_None` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 142 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 113 | 37 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 161 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 279 | 203 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 169 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 96–110 | 15 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 98–220 | 123 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 105–204 | 70 | 3 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 138–169 | 32 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 141–299 | 155 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 141–299 | 159 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 144–299 | 156 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 160–177 | 18 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 162–166 | 5 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 164–299 | 131 | 3 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 197–222 | 12 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 204–299 | 93 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 208–299 | 92 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 229–281 | 53 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 235–287 | 44 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 275–299 | 25 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 288–299 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [77–95], lower_priority='Action_DownBlock' annotated_start=79, effective_Action_DownBlock_start=96.
- ⚠️ Action 'Action_None' range [77-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [79-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [106-109] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [81-156] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [159-163] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-142] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-253] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-274] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-279] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-198] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [79-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [136-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-119] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-204] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-246] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-170] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-281] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-271] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-287] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '32' has 1 frames without a visible bounding box.
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

</details>