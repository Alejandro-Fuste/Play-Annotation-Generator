# Play-Annotation-Generator Annotation Review — Counter_306

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_306`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 1
- **Action Segments:** 104
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `3` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 78 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `3` | 79 | START | 79 | 93 |
| ✅ EXACT | `Action_DownBlock` | RT | `10` | `9` | 82 | START | 82 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `4` | `3` | 82 | START | 94 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `11` | `10` | 82 | START | 82 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `8` | `7` | 82 | START | 82 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `15` | `14` | 93 | END | 79 | 84 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 103 | START | 103 | 125 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `20` | `17` | 130 | START | 130 | 233 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 102 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 103 | 125 | 23 | inferred_complete_timeline |
| `Action_None` | 173 | 249 | 77 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 267 | 270 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 131 | 53 | inferred_complete_timeline |
| `Action_None` | 134 | 179 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 78 | 45 | inferred_complete_timeline |
| `Action_None` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_None` | 99 | 127 | 29 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 82 | 115 | 34 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 117 | 167 | 51 | inferred_complete_timeline |
| `Action_None` | 168 | 329 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 98 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 115 | 120 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallSnap` | 79 | 93 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 139 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 167 | 20 | inferred_complete_timeline |
| `Action_None` | 168 | 193 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 90 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_None` | 136 | 150 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 167 | 86 | inferred_complete_timeline |
| `Action_None` | 168 | 329 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 153 | 75 | inferred_complete_timeline |
| `Action_None` | 174 | 186 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 329 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 329 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 113 | 35 | inferred_complete_timeline |
| `Action_None` | 119 | 124 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 164 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 175 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 329 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 329 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_None` | 79 | 329 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | Position_Unknown | Team_Unknown | 94–233 | 140 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 113–329 | 212 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 151–329 | 155 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 151–211 | 43 | 6 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 161–172 | 9 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 188–191 | 4 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 197–329 | 128 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 210–263 | 54 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 217–254 | 38 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 242–262 | 21 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 242–329 | 88 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 251–329 | 74 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 253–329 | 77 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 257–259 | 3 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 261–329 | 60 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 281–320 | 40 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 0 | 68 | 30 | 43.5% | 6–14, 16–17, 33, 36, 39–46, 50–67 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [79–93], lower_priority='Action_DownBlock' annotated_start=82, effective_Action_DownBlock_start=94.
- ⚠️ Action 'Action_None' range [79-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-146] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-193] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [82-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [117-167] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-131] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [100-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [115-120] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-164] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [79-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [103-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-249] for track '14' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-127] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-233] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-169] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-166] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-246] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-329] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-263] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-254] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-263] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-319] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-285] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-320] for track '33' has 1 frames without a visible bounding box.
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

</details>